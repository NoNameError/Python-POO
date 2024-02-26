from datetime import datetime, timedelta

class PF:
    def __init__(self, nome, cpf, data_entrada, media_salarial):
        self.nome = nome
        self.cpf = cpf
        self.data_entrada = datetime.strptime(data_entrada, '%d/%m/%Y')
        self.media_salarial = media_salarial

    def credit_limit(self):
        if datetime.now() - self.data_entrada >= timedelta(days=90):
            return self.media_salarial * 0.4
        else:
            return 'inválido'

    def __str__(self):
        return f'Seu nome: {self.nome}\nCPF: {self.cpf}\nAdmissão: {self.data_entrada}\nSalario Medio do Funcionario: {self.media_salarial}'

class PJ:
    def __init__(self, fantasia, cnpj, data_criacao, faturamento):
        self.fantasia = fantasia
        self.cnpj = cnpj
        self.data_criacao = datetime.strptime(data_criacao, '%d/%m/%Y')
        self.faturamento = faturamento

    def credit_limit(self):
        if datetime.now() - self.data_criacao >= timedelta(days=450):
            return self.faturamento * 0.4
        else:
            return 'inválido'

    def __str__(self):
        return f'Nome Fantasia: {self.fantasia}\nCNPJ: {self.cnpj}\nData de criação: {self.data_criacao}\nFaturamento: {self.faturamento}'

def main():
    while True:
        print('Bem vindo à KaraliusCorp, é um prazer ter você aqui!')
        contrato = input('Informe qual o seu vínculo empregatício\n(1 - Pessoa Física)\n(2 - Pessoa Jurídica)\n')

        if contrato == '1':
            nome = input('Nome: ')
            cpf = input('CPF: ')
            data_entrada = input('Data de admissão (DDMMAAAA): ')
            data_entrada_formatada = f"{data_entrada[:2]}/{data_entrada[2:4]}/{data_entrada[4:]}"
            salario = float(input('Média Salarial dos últimos 3 meses: '))
            pessoa = PF(nome, cpf, data_entrada_formatada, salario)
            break

        elif contrato == '2':
            nome_fantasia = input('Nome fantasia: ')
            cnpj = input('CNPJ: ')
            criacao = input('Data de criação (DD/MM/AAAA): ')
            faturamento = float(input('Faturamento nos últimos 15 meses: '))
            pessoa = PJ(nome_fantasia, cnpj, criacao, faturamento)
            break

        else:
            print('Opção inválida ou Inexistente, por favor, selecione apenas as opções indicadas.\n')

    credit_limit = pessoa.credit_limit()
    if credit_limit != 'inválido':
        print('Parabéns, o seu cartão de crédito está aprovado!')
        print(f'Limite de crédito de: R$ {credit_limit:.2f}')
    else:
        print('Desculpe, o seu cartão não foi aprovado, mas não desanime, volte novamente em 3 meses!')

    print('\nInformações do cliente:')
    print(pessoa)

if __name__ == '__main__':
    main()