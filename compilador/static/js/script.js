if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}

function novoAF() {
  let x = document.getElementById("criar_automato")
  if (x.style.display === "none") {
    x.style.display = "block"
  } else {
    x.style.display = "none"
  }
}

var numeroEstados = 1 // Contador da ordem de transições

function adiconarEstado() {
  numeroEstados++
  let x = document.getElementById("estrutura_estados")
  let linha =
    '<tr id="linha_tabela_'+numeroEstados+'"> \
      <td>'+numeroEstados+'</td> \
      <td><input type="text" name="nome_estado'+numeroEstados+'" required /></td> \
      <td> \
        <select name="tipo_estado'+numeroEstados+'"> \
          <option value="0">Inicial</option> \
          <option value="1">Normal</option> \
          <option value="2">Final</option> \
          <option value="3">Inicial e Final</option> \
        </select> \
      </td> \
    </tr>'
  x.innerHTML += linha
  document.getElementById("num_vals").value = numeroEstados
}

function removerEstado() {
  if (numeroEstados > 0) {
    let x = document.getElementById("linha_tabela_"+numeroEstados)
    x.parentNode.removeChild(x)
    numeroEstados = ((numeroEstados == 1) ? 0 : numeroEstados-1)
    document.getElementById("num_vals").value = numeroEstados
  }
}

function submitFormEstados() {
  var form = document.getElementById("form_estados");
  var data = new FormData(form);
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("POST", "");
  xmlhttp.send(data);
  return false
}
