// 문서 로딩이 끝나면 호출되는 함수 등록
window.onload = function(){
    //삭제 버튼을 클릭하면 수행하는 함수 등록
    document.getElementById('btnDel').addEventListener('click', function(){
        confirm("정말 삭제하시겠습니까?") && document.forms['formDelete'].submit();
    });
}