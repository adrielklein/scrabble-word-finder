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
            num_words = words.length
            sing_or_plu = (num_words == 1) ? " word: " : " words: "
            message = "Found " + num_words + sing_or_plu;
            displayMessage(message);
            displayWords(getList(words));
         }
    }
}

function getList(array) {
    var listElements = ""
    for (var i = 0; i < array.length; i++) {
        listElements += "<li>" + array[i] + "</li>"
    }
    return "<ul>" + listElements + "</ul>";
}

function displayMessage(value) {
    document.getElementById("message").innerHTML = value
}
function displayWords(words) {
    document.getElementById("list-of-words").innerHTML = words
}