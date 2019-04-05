function check() {
    url = document.getElementById("url").value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/' + encodeURIComponent(url), true);
    xhr.send();
    xhr.onreadystatechange = function() {
        document.getElementById("message").innerText = xhr.responseText;
    }
}
