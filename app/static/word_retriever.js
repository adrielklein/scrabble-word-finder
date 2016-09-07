function showWords() {
    var word = document.getElementById("word").value;
    var url = "/words/" + word;

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = processRequest;
    xhr.open("GET", url, true);
    xhr.send();

    function processRequest(e) {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var words = JSON.parse(xhr.responseText)["words"];
            var word = document.getElementById("word").value;
            document.getElementById("panel-title").innerHTML = getPanelTitle(words.length);
            document.getElementById('resultsDiv').style.display = "block";
            document.getElementById("list-of-words").innerHTML = getHTMLList(words)
         }
    }
}

function getPanelTitle(numWords){
    var word = document.getElementById("word").value;
    return "Words for " + word + "<span id='badge' class='badge'> "+ numWords +"</span>";
    }

function getHTMLList(array) {
    var listElements = ""
    for (var i = 0; i < array.length; i++) {
        listElements += "<li class='list-group-item'>" + array[i] + "</li>"
    }
    return "<ul>" + listElements + "</ul>";
}

