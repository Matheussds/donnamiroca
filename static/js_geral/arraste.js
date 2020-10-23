var itemSelecao = document.querySelectorAll(".item-selecao");
var contador = 0;

itemSelecao.forEach(element => {
    var idItem = "item" + contador;
    element.setAttribute("draggable", "true");
    element.setAttribute("ondragstart", "drag(event)");
    element.setAttribute("id", idItem)
    contador++;
    console.log(idItem);
  });

function allowDrop(ev) {
    ev.preventDefault();
  }
  
  function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
  }
  
  function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var item_select = document.getElementById(data);

    ev.currentTarget.appendChild(item_select);
    
    
    if (item_select.childElementCount == 1) {
      var form_unid = document.createElement("form");
      var input_unid = document.createElement("input");
      var label_unid = document.createElement("label");
      input_unid.setAttribute("type", "number");
      input_unid.setAttribute("value", "1");
      input_unid.setAttribute("maxlength", "3");
      label_unid.innerHTML = "Qtd.&nbsp&nbsp";
      item_select.appendChild(form_unid);
      form_unid.appendChild(label_unid);
      form_unid.appendChild(input_unid);
    }
    
  }

  function drop2(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var item_select = document.getElementById(data);

    ev.currentTarget.appendChild(item_select);
    item_select.removeChild(item_select.childNodes[3]);
  }