document.addEventListener('DOMContentLoaded',function (e) {
    inputs = document.getElementsByTagName('input')
    buttons = document.getElementsByTagName('button')
    selects = document.getElementsByTagName('select')
    textareas = document.getElementsByTagName('textarea')
    images = document.getElementsByTagName('img')

    console.log(images)

    /*
    hrefs = document.getElementsByTagName('a')
    console.log(inputs)
    class="form-control-lg"
    btn btn-primary
    text-info
    007bff
    */
/*
    for(let x=0;x<feature.children.length;x++){
        feature.children[x].style.height = '20px'
    }*/

    for(let x=0;x<inputs.length;x++){
        inputs[x].setAttribute('class',"form-control p-3 mb-2 bg-light text-dark");

        inputs[x].style.width = '600px';
        inputs[x].style.height = '50px';
    }


    for(let x=0;x<buttons.length;x++){
        buttons[x].setAttribute('class',"btn btn-outline-primary");
    }


    for(let x=0;x<selects.length;x++){
        selects[x].setAttribute('class',"form-control form-control-lg  p-3 mb-2 bg-light text-dark");
        selects[x].style.width = '600px';
        selects[x].style.height = '50px';
    }

    
    
    for(let x=0;x<textareas.length;x++){
        textareas[x].setAttribute('class',"form-control p-3 mb-2 bg-light text-dark");
        textareas[x].setAttribute('rows',"3");
        textareas[x].style.width = '600px';
    }

    for(let x=0;x<images.length;x++){
        images[x].setAttribute('class',"img-rounded ");
        images[x].setAttribute('width',400)
        images[x].setAttribute('height',300)
    }



})