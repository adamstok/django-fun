
document.addEventListener('DOMContentLoaded',function (e) {
    inputs = document.getElementsByTagName('input')
    buttons = document.getElementsByTagName('button')

    for(let x=0;x<inputs.length;x++){
        inputs[x].setAttribute('class',"form-control")
    }

    for(let x=0;x<buttons.length;x++){
        buttons[x].setAttribute('class',"btn btn-primary")
    }

  })