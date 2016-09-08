$(document).ready(function(){
    $("button").click(function(){
        setWordPanel()
    });
});


function setWordPanel(){
    var letters = document.getElementById("letters").value;
    var url = "/words/" + letters;

    $.getJSON(url, setWordPanelFurther);
}

function setWordPanelFurther(response){
    var words = response['words'];
    panelTitle = getPanelTitle(words.length)
    listOfWords = getHTMLList(words)
    var panelId = new Date().getTime()
    var collapseId = panelId +1
    wordPanel = getWordPanel(panelTitle, listOfWords, panelId, collapseId);

    $("#word-panels").append(wordPanel);

    $(function(){
    $("#" + collapseId).on('click',function(){
        $("#" + panelId).remove();
    })
})
}

function getWordPanel(panelTitle, listOfWords, panelId, collapseId){
    var toggleId = collapseId + 1;
    return '<div id="'+panelId+'" class="container" style="width:320px;">\
            <div class="panel-group">\
                <div class="panel panel-default">\
                    <div class="panel-heading">\
                        <h4 class="panel-title">\
                            <a data-toggle="collapse" href="#'+toggleId+'">'+panelTitle+'</a>\
                             <span id="'+collapseId+'" class="pull-right" data-effect="slideUp"><i class="fa fa-times"></i></span>\
                         </h4>\
                     </div>\
                     <div id="'+toggleId+'" class="panel-collapse collapse">\
                        <ul class="list-group">'+listOfWords+'</ul>\
                    </div>\
                </div>\
            </div>\
        </div>'
}

function getPanelTitle(numWords){
    var letters = document.getElementById("letters").value;
    return letters + "<span id='badge' class='badge'> "+ numWords +" words</span>";
}

function getHTMLList(array) {
    var listElements = ""
    for (var i = 0; i < array.length; i++) {
        listElements += "<li class='list-group-item'>" + array[i] + "</li>"
    }
    return listElements
}

