// O cookie clicker é um jogo em que o objetivo é chegar ao número X o mais rápido possível, sabemos que
// a cada segundo são produzidos 2 cookies, e quando chegamos ao custo C de uma fazenda podemos comprá-la,
// pagamos essa fazenda com os cookies, cada fazenda lhe dá uma produção, que é anexada a esses 2 cookies 
// por segundo, sendo assim o jogo consiste em saber quando compensa ou não comprar mais uma fazenda ou 
// apenas esperar para que chegue até o objetivo final.

//Variáveis de parametro:
//	-	C: Custo de cada fazenda;
//	-	F: Produção de cada fazenda;
//	-	X: Objetivo final;

// Essa função recebe os parâmetros descritos acima e retorna o tempo necessário em segundos para atingir o objetivo.
function cookie_clicker(c,f,x){
 	//Verifica se a saída esperada é de 1 ou 2 cookies, nesse caso,
 	//não é necessário calcular.
 	if(x <= 2){
 	 	return 1;
 	}
 	var aux = x;
 	var tempo = 0;
 	var cookie = 2;
 	// Enquanto o objetivo for maior que o custo de cada fazenda compramos fazendas
 	while(x >= c){
	 	if(x >= c){
	 	 	tempo += c / cookie;
	 	 	cookie += f;
	 	 	x = x - c;
	 	}
 	}
 	// Aqui ele calcula o tempo restante para atingir o objetivo, dado a que a produção dos cookies já foi
 	// elevada pela compra das fazendas.
 	var resposta = (tempo+((aux-c)/(cookie-f)));
 	return resposta;
}

// Leitura e saída 
var fs = require("fs");
var entrada = fs.readFileSync("B-small-pratice.in").toString().split("\n");
for(var i = 0; i < 100; i++){
	var parametros = entrada[i].split(" ");
	var res = cookie_clicker(parseFloat(parametros[0]), parseFloat(parametros[1]), parseFloat(parametros[2]));
	console.log("Case #"+(i+1)+": "+res);
}