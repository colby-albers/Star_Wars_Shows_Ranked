function accept(id) {
    var element = document.querySelector(id);
    element.remove();
}

function changePic(element){
    console.log(element.getAttribute("src"))
    if(element.getAttribute("src") == "{{url_for('static', filename=boba_score.PNG")
    {
        element.setAttribute("src", "boba_fett.jpg")
    }
    else{
        element.setAttribute("src", "{{url_for('static', filename=boba_score.PNG")
    }
}

function changePic2(element){
    console.log(element.getAttribute("src"))
    if(element.getAttribute("src") == "obi_score.PNG"){
        element.setAttribute("src", "obi-wan.jpg")
    }
    else{
        element.setAttribute("src", "obi_score.PNG")
    }
}

function changePic3(element){
    console.log(element.getAttribute("src"))
    if(element.getAttribute("src") == "batch_score.PNG"){
        element.setAttribute("src", "bad_batch.jpg")
    }
    else{
        element.setAttribute("src", "batch_score.PNG")
    }
}
function changePic4(element){
    console.log(element.getAttribute("src"))
    if(element.getAttribute("src") == "clone_score.PNG"){
        element.setAttribute("src", "clone-wars.jpg")
    }
    else{
        element.setAttribute("src", "clone_score.PNG")
    }
}
function changePic5(element){
    console.log(element.getAttribute("src"))
    if(element.getAttribute("src") == "mando_score.PNG"){
        element.setAttribute("src", "mandalorian.jpg")
    }
    else{
        element.setAttribute("src", "mando_score.PNG")
    }
}
function changePic6(element){
    console.log(element.getAttribute("src"))
    if(element.getAttribute("src") == "andor_score.PNG"){
        element.setAttribute("src", "andor.jpg")
    }
    else{
        element.setAttribute("src", "andor_score.PNG")
    }
}
function changePic7(element){
    console.log(element.getAttribute("src"))
    if(element.getAttribute("src") == "visions_score.PNG"){
        element.setAttribute("src", "visions.jpeg")
    }
    else{
        element.setAttribute("src", "visions_score.PNG")
    }
}
function changePic8(element){
    console.log(element.getAttribute("src"))
    if(element.getAttribute("src") == "rebels_score.PNG"){
        element.setAttribute("src", "rebels.jpg")
    }
    else{
        element.setAttribute("src", "rebels_score.PNG")
    }
}