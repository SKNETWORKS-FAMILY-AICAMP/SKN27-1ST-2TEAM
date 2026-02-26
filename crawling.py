import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def run_kia_integrated_crawler():
    async with async_playwright() as p:
        print("🌐 [1/5] uv 환경에서 정밀 크롤러를 시작합니다...")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 1024})
        page = await context.new_page()
        
        url = "https://www.car.go.kr/rs/faq/list.do"
        print(f"🔗 [2/5] 사이트 접속: {url}")
        await page.goto(url, wait_until="domcontentloaded")
        
        print("⏳ [3/5] 페이지 안정화 대기 (7초)...")
        await page.wait_for_timeout(7000)

        # 카테고리 반복문 없이 바로 수집 시작
        all_faq_results = []
        current_page = 1

        print("🚀 [4/5] 다중 페이지 수집 모드 가동 중...")

        while True:
            print(f"\n📄 {current_page}페이지 수집 중...")
            
            # 1. 페이지 안정화 대기
            await page.wait_for_timeout(4000)

            # 2. 현재 페이지의 질문들(.uk-accordion-title) 수집
            titles = await page.query_selector_all(".uk-accordion-title")
            
            # 만약 해당 페이지에 질문이 하나도 없다면 종료
            if not titles:
                print(f"🏁 더 이상 수집할 항목이 없습니다. (현재: {current_page}페이지)")
                break

            page_count = 0
            for title_el in titles:
                question_text = (await title_el.inner_text()).strip()
                
                # 답변 추출 (형제 요소 .uk-accordion-content)
                content_el = await title_el.evaluate_handle("el => el.nextElementSibling")
                
                answer_combined = "상세 내용 없음"
                if content_el:
                    elements = await content_el.as_element().query_selector_all("p, li, #container-619af8ccc1 li")
                    if elements:
                        texts = [f"• {(await el.inner_text()).strip()}" for el in elements if (await el.inner_text()).strip()]
                        answer_combined = "\n".join(texts)
                
                all_faq_results.append({
                    "페이지": current_page,
                    "질문": question_text,
                    "답변": answer_combined
                })
                page_count += 1
            
            print(f"   ✅ {current_page}페이지에서 {page_count}건 수집 완료.")

            # 3. 다음 페이지로 이동 ($main.event.fn_search 실행)
            current_page += 1
            print(f"   ➔ {current_page}페이지로 이동 시도 중...")
            
            try:
                # 자바스크립트 함수 직접 실행
                # return false;가 붙어있으므로 evaluate를 통해 실행합니다.
                success = await page.evaluate(f"() => {{ $main.event.fn_search({current_page}); return false; }}")
                
                # 페이지 로딩 시간 확보
                await page.wait_for_timeout(3000)
                
                # 다음 페이지로 넘어갔을 때 이전 페이지와 똑같은 데이터라면 중단하는 안전장치
                # (실제 사이트 구조에 따라 조정이 필요할 수 있습니다.)
            except Exception as e:
                print(f"   🛑 페이지 이동 중 오류 또는 끝 도달: {e}")
                break

        print(f"\n✨ 수집 종료! 총 {len(all_faq_results)}건의 데이터를 통합했습니다.")

        # 5. 최종 데이터 저장
        print("\n" + "="*50)
        if all_faq_results:
            df = pd.DataFrame(all_faq_results)
            output_file = "faq.csv"
            df.to_csv(output_file, index=False, encoding='utf-8-sig')
            print(f"✨ [5/5] 수집 완료! 총 {len(df)}행의 데이터가 생성되었습니다.")
            print(f"💾 저장된 파일: {output_file}")
        else:
            print("❌ 데이터가 비어있습니다.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_kia_integrated_crawler())