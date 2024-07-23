from sistema_conta_corrente import Conta_corrente, CartaoCredito
from agencia import Agencia


#cria uma nova instancia de conta corrente
conta_denner = Conta_corrente("Denner",'100.555.668-15',1234,34062)
#cria uma nova instancia de cartao de credito
cartao_denner = CartaoCredito('Denner',conta_denner)

agencia1 = Agencia(222224,26266369,4568)

