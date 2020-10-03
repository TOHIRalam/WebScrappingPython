$(document).ready(function(){
   $.ajax({
       url: "news.csv",
       dataType: "text",
       success: function(data) {
        var employee_data = data.split(/\r?\n|\r/);
        for(var i = 1; i < employee_data.length-1; i++) {
            var str = "news";
            addList(employee_data[i], str+i, 1);
        }
       }
   });

   $.ajax({
       url: "bbcNews.csv",
       dataType: "text",
       success: function(data) {
        var employee_data = data.split(/\r?\n|\r/);
        for(var i = 1; i < employee_data.length-1; i++) {
            var str = "bbc";
            addList(employee_data[i], str+i, 2);
        }
       }
   });


   $.ajax({
       url: "newsLink.csv",
       dataType: "text",
       success: function(data) {
        var link = data.split(/\r?\n|\r/);
        for(var i = 1; i < link.length-1; i++) {
            document.getElementById('news'+i).setAttribute('href', link[i]);
        }
       }
   });

   $.ajax({
       url: "bbcNewsLink.csv",
       dataType: "text",
       success: function(data) {
        var link = data.split(/\r?\n|\r/);
        for(var i = 1; i < link.length-1; i++) {
            document.getElementById('bbc'+i).setAttribute('href', link[i]);
        }
       }
   });

});

function addList(data, id, ulNumber) {
    var ulNode = document.getElementById('listUl' + ulNumber);
    var listNode = document.createElement("li");
    var aNode = document.createElement("a");
    var textNode = document.createTextNode(data);
    listNode.appendChild(aNode);
    aNode.appendChild(textNode);
    ulNode.appendChild(listNode);
    aNode.setAttribute("id", id);
    aNode.setAttribute("target", "blank");
}