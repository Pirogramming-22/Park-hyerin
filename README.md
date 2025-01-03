# 피로그래밍 22기 박혜린 과제 제출 레포포
🍀주차별 과제의 챌린지 및 추가 구현에 대한 설명이 있습니다🍀
<br>
## 2주차
▫️ python_problem
- choice 1의 경우(입력 받은 학생 정보에서 데이터 입력 갯수, 이미 존재하는 이름, 점수 값의 양의 정수인지 판별)
: 입력값의 점수가 단순 양의 정수가 아닌 100 초과를 할 경우에는 예외 처리를 하도록 함

            if not score1.isdigit() or not score2.isdigit(): //0이거나 소수점이 있거나, 음수의 경우 예외처리
                ...      
            s1 = int(score1)
            s2 = int(score2)
            if s1 > 100 or s2 > 100 //100초과의 점수인 경우 예외처리
                ... 

▫️ Javascript 스톱워치 과제
-  전체 선택 버튼 기능
// stop_record의 아이콘을 통해 전체 기록을 선택 및 선택 해제하는 함수
const toggleAllRecordSelection = () => {
    // 전체 선택 아이콘이 현재 '체크됨' 상태인지 확인
    
    if (allChecked) {     
        // stop_record 아이콘이 체크됨 상태였다면 체크되지 않음으로 바꾸고 각 기록들의 아이콘을 체크되지 않음으로 만듦
        ...
    } else {
        // stop_record 아이콘이 체크되지 않은 상태였다면 체크됨으로 바꾸고 각 기록들의 아이콘을 체크됨으로 만듦
    }
    syncSelectAllIconState(); // 선택된 기록 상태에 맞게 전체 선택 아이콘의 상태를 동기화(뒤에 이어질 함수에서 사용용)
};
// 선택된 기록의 수가 전체 기록의 수와 같으면 stop_record의 아이콘을 '체크됨' 상태로 만들어주는 함수
const syncSelectAllIconState = () => {
    // 기록의 전체 개수(totalRecords)와 선택된 개수(selectedCount) 확인
    if (selectedCount === totalRecords) { //stop_record의 아이콘을 '체크됨'으로 변경
        checkboxIcon.classList.replace('ri-checkbox-blank-circle-line', 'ri-checkbox-circle-line');
    } else {                             // stop_record의 아이콘을 '체크되지 않음음'으로 변경
        checkboxIcon.classList.replace('ri-checkbox-circle-line', 'ri-checkbox-blank-circle-line');
    }
};
