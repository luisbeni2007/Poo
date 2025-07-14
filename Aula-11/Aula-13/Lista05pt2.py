from datetime import datetime
from enum import Enum

class pagamento (Enum):
    EmAberto = 0 
    PagoParcial = 1
    Pago = 2

class boleto ():
    def __init(self, cod: str, emissao: datetime, venc: datetime, valor: float):
        self.__codBarras = cod
        self.__dateEmissao = emissao
        self.__DataVencimento = venc
        self.__dataPago = None
        self.__valorBoleto = valor
        self.__valorPago = 0.0
        self.__situacaoPagamento = pagamento.EmAberto


    def get_cod_barras(self):
        return self.__codBarras
    
    def get_date_Emissao(self):
        return self.__dateEmissao
    
    def get_Data_Vencimento(self):
        return self.__DataVencimento

    def get_dataPago(self):
        return self.__dataPago
    
    def get_valorBoleto(self):
        return self.__valorBoleto
    
    def get_valorPago(self):
        return self.__valorPago
    
    def get_situacaoPagamento(self):
        return self.__situacaoPagamento
    

    def set_cod_barras(self,cod):
        self.__codBarras = cod
    
    def set_data_emissao(self,emissao):
        self.__dateEmissao = emissao

    def set_data_vencimento(self, vencimento):
        self.__DataVencimento = vencimento

    def set_valor_boleto(self,valor):
        self.__valorBoleto = valor


    def pagar(self, valorPago: float):
        if valorPago <= 0:
            print("valor pago deve ser positivo")
            return
        self.__valorPago += valorPago
        self.__dataPago = datetime.now()

        if self.__valorPago == 0:
            self.__situacaoPagamento = pagamento.EmAberto
        elif self.__valorPago < self.__valorBoleto:
            self.__situacaoPagamento = pagamento.PagoParcial
        elif self.__valorPago >= self.__valorBoleto:
            self.__situacaoPagamento = pagamento.Pago

    def situacao(self):
        return self.__situacaoPagamento

    def __str__(self):
        data_pago_str = self.__dataPago.strftime('%d/%m/%Y %H:%M:%S') if self.__dataPago else "Não pago"
        return (
            f"Código de Barras: {self.__codBarras}\n"
            f"Data de Emissão: {self.__dateEmissao.strftime('%d/%m/%Y')}\n"
            f"Data de Vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}\n"
            f"Valor do Boleto: R$ {self.__valorBoleto:.2f}\n"
            f"Valor Pago: R$ {self.__valorPago:.2f}\n"
            f"Data do Pagamento: {data_pago_str}\n"
            f"Situação: {self.__situacaoPagamento.name}"
        )

if __name__ == "__main__":
    print("=== Cadastro de Boleto ===")
    cod = input("Código de Barras: ")
    emissao_str = input("Data de Emissão (dd/mm/aaaa): ")
    venc_str = input("Data de Vencimento (dd/mm/aaaa): ")
    valor = float(input("Valor do Boleto: R$ "))

    try:
        emissao = datetime.strptime(emissao_str, "%d/%m/%Y")
        venc = datetime.strptime(venc_str, "%d/%m/%Y")
    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa.")
        exit()

    boleto = boleto(cod, emissao, venc, valor)

    print("\n--- Dados do Boleto ---")
    print(boleto)

    while True:
        pagar = input("\nDeseja registrar um pagamento? (s/n): ").lower()
        if pagar == 's':
            valor_pagamento = float(input("Valor a pagar: R$ "))
            boleto.pagar(valor_pagamento)
            print("\n--- Dados atualizados do Boleto ---")
            print(boleto)
        else:
            print("\nEncerrando programa.")
            break