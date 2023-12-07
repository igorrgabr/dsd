from spyne import Application, rpc, ServiceBase, Iterable, Unicode, Integer, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CardapioItem(ComplexModel):
    _type_info = {
        'item_id': Unicode,
        'descricao': Unicode,
        'valor': Integer,
    }

class RestauranteService(ServiceBase):
    cardapio = {
        '1': {'descricao': 'Pizza', 'valor': 30},
        '2': {'descricao': 'Hambúrguer', 'valor': 14},
        '3': {'descricao': 'Salada', 'valor': 10},
        '4': {'descricao': 'Batata Frita', 'valor': 12},
        '5': {'descricao': 'Refrigerante', 'valor': 8},
        '6': {'descricao': 'Suco', 'valor': 6},
        '7': {'descricao': 'Água', 'valor': 2}
    }

    mesas = {'01': 'aberta', '02': 'aberta', '03': 'aberta', '04': 'fechada', '05': 'aberta', '06': 'fechada', '07': 'aberta', '08': 'fechada'}

    pedidos = {}

    @rpc(_returns=Iterable(Unicode))
    def obter_mesas(ctx):
        mesas_abertas = [mesa_id for mesa_id, status in RestauranteService.mesas.items() if status == 'aberta']
        return mesas_abertas

    @rpc(Unicode, _returns=Unicode)
    def reservar_mesa(ctx, mesa_id):
        if mesa_id not in RestauranteService.mesas:
            return "Mesa inexistente!"
        elif RestauranteService.mesas[mesa_id] == 'aberta':
            RestauranteService.mesas[mesa_id] = 'fechada'
            return f"Mesa {mesa_id} reservada com sucesso!"
        else:
            return f"Mesa {mesa_id} já está ocupada!"

    @rpc(_returns=Iterable(CardapioItem))
    def obter_cardapio(ctx):
        cardapio_items = []
        for item_id, info in RestauranteService.cardapio.items():
            cardapio_items.append(CardapioItem(item_id=item_id, descricao=info['descricao'], valor=info['valor']))
        return cardapio_items

    @rpc(Unicode, Unicode, Integer, _returns=Unicode)
    def fazer_pedido(ctx, mesa_id, item_id, quantidade):
        if item_id not in RestauranteService.cardapio:
            return "Item não encontrado no cardápio."
        else:
            descricao = RestauranteService.cardapio[item_id]['descricao']
            valor_unitario = RestauranteService.cardapio[item_id]['valor']
            valor_total = valor_unitario * quantidade

            pedido_info = f"{descricao} (Quantidade: {quantidade}, Valor Unitário: {valor_unitario}, Valor Total: {valor_total})"
            if mesa_id not in RestauranteService.pedidos:
                RestauranteService.pedidos[mesa_id] = []

            RestauranteService.pedidos[mesa_id].append(pedido_info)

            return f"Pedido realizado com sucesso. Detalhes: {pedido_info}"

    @rpc(Unicode, _returns=Unicode)
    def fechar_conta(ctx, mesa_id):
        if mesa_id in RestauranteService.pedidos:
            conta = RestauranteService.pedidos[mesa_id]
            total = sum(
                float(pedido.split('Valor Total: ')[1][:-1]) for pedido in RestauranteService.pedidos[mesa_id])
            del RestauranteService.pedidos[mesa_id]
            RestauranteService.mesas[mesa_id] = 'aberta'
            return f"Conta fechada para Mesa {mesa_id}: {conta} Total: {total}"
        else:
            return f"Mesa {mesa_id} não possui pedidos."

app = Application([RestauranteService], 'Restaurante',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 1234, wsgi_app)
    print("Servidor SOAP rodando na porta 1234...")
    server.serve_forever()