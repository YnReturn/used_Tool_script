var importJs=document.createElement('script')
importJs.setAttribute("type","text/javascript")
importJs.setAttribute("src", 'https://ajax.microsoft.com/ajax/jquery/jquery-1.4.min.js')
document.getElementsByTagName("head")[0].appendChild(importJs)
var $i = 0


window.setInterval(async() =>{
    await $(".Scroll_container_280Ky button[index='"+$i+"']").click();//确定窗口
    await $(".woo-modal-main button + button").click();//确定确认按钮
    $i++;
    console.log($i);
},606)

/*
不知道为什么，取消关注都是隔开一位，然后必须滑轮（这个应该是网页不滑动，没有得到了刷新，无法获取元素）
*/
