const soap = require('soap');
const readline = require('readline');

const url = 'http://127.0.0.1:1234/?wsdl';

console.log("Bem-vindo ao Restaurante 5-Star SOAP!");
let mesaReservadaId;

soap.createClient(url, (err, client) => {
  if (err) {
    console.error(err);
    return;
  }

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  // Exibe mesas disponíveis
  client.obter_mesas((err, result) => {
    if (err) {
      console.error(err);
      return;
    }
    if (result.obter_mesasResult === null || !result.obter_mesasResult) {
      console.log('Nenhuma mesa disponível :(\nVolte mais tarde!');
      rl.close();
      return;
    }
    console.log('Mesas disponíveis:', result.obter_mesasResult.string);
    reservarMesa(result.obter_mesasResult.string);
  });

  // Reservar mesa
  function reservarMesa(mesasDisponiveis) {
    rl.question('Informe o número da mesa para reservar (ex.: 01): ', (mesaNumero) => {
      const mesaId = mesaNumero.trim();
      if (mesasDisponiveis.includes(mesaId)) {
        client.reservar_mesa({ mesa_id: mesaId }, (err, result) => {
          if (err) {
            console.error(err);
            return;
          }
          console.log(result.reservar_mesaResult);
          if (result.reservar_mesaResult.includes("reservada com sucesso")) {
            mesaReservadaId = mesaId;
            exibirCardapio();
          } else {
            console.log(result.reservar_mesaResult);
            reservarMesa(mesasDisponiveis);
          }
        });
      } else {
        console.log('Número de mesa inválido. Tente novamente.');
        reservarMesa(mesasDisponiveis);
      }
    });
  }

  // Exibe o cardápio
  function exibirCardapio() {
    client.obter_cardapio((err, result) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log('Itens do cardápio:', result.obter_cardapioResult.CardapioItem);
      realizarAcao();
    });
  }

  // Escolhas do usuário
  function realizarAcao() {
    rl.question('Escolha uma opção:\n1. Fazer pedido\n2. Fechar a conta\nOpção: ', (opcao) => {
      switch (opcao) {
        case '1':
          fazerPedido();
          break;
        case '2':
          fecharConta();
          break;
        default:
          console.log('Opção inválida. Tente novamente.');
          realizarAcao();
      }
    });
  }

  // Fazer pedido
  function fazerPedido() {
    rl.question('Informe os detalhes do pedido, no formato: item_id quantidade ', (pedidoParams) => {
      const [item_id, quantidade] = pedidoParams.split(' ');
      client.fazer_pedido({ mesa_id: mesaReservadaId, item_id, quantidade }, (err, result) => {
        if (err) {
          console.error(err);
          return;
        }
        console.log(result.fazer_pedidoResult);
        realizarAcao();
      });
    });
  }

  // Fechar a conta
  function fecharConta() {
    client.fechar_conta({ mesa_id: mesaReservadaId }, (err, result) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(result.fechar_contaResult);
      rl.close();
    });
  }
});
