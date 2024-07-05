for i in range(1,13):
    with open(f'{i}월_보고서.txt','w',encoding='utf-8') as file:
        file.write(f'{i}월 보고서\n')
        file.write('작성자:\n')
        file.write('주요 내용:\n')
        file.write('결과 및 피드백:\n')
        