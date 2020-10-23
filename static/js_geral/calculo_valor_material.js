var v_input_pacote = document.getElementById('valor_pacote_m');
var v_input_unidade = document.getElementById('valor_unidade_m');
var v_quantidade = document.getElementById('quantidade_m');
var v_numero_formatado;

function mudarTipoNumero() {
    var id_medida = document.getElementById('unidade_m').value;
    if (id_medida == 1) {
        console.log('mudando para int');
        v_numero_formatado = parseInt(v_quantidade.value);
    } else {
        console.log('mudando para float');
        v_numero_formatado = parseFloat(v_quantidade.value);
    }
}

function valorUnidade() {
    mudarTipoNumero();
    if (v_quantidade.value >= 1) {
        v_input_unidade.value = parseFloat(parseFloat(v_input_pacote.value.replace(',', '.')) / v_numero_formatado).toFixed(2);
    }
}

function valorPacote() {
    mudarTipoNumero();
    if (v_quantidade.value >= 1) {
        v_input_pacote.value = parseFloat(parseFloat(v_input_unidade.value.replace(',', '.')) * v_numero_formatado).toFixed(2);
    }
}
