from validate_docbr import CPF,CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) ==14:
            return DocCnpj(documento)
        else:
            raise ValueError ("Quantidade de dígitos está incorreta")

class DocCpf:
    def __init__(self,documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError ("CPF Inválido")

    def __str__(self):
        return self.format()

    def valida(self,documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self,documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError ("CNPJ Inválido")

    def __str__(self):
        return self.format()

    def valida(self,documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)



### Versão Antiga
# class CpfCnpj:
#     def __init__(self,documento,tipo_documento): #Agora, precisamos informar qual o tipo de documento vamos utilizar, se é cpf ou cnpj
#         self.tipo_documento = tipo_documento
#         documento = str(documento)
#         if self.tipo_documento == "cpf":
#             if self.cpf_eh_valido(documento):
#                 self.cpf = documento
#             else:
#                 raise ValueError("CPF inválido")
#         elif self.tipo_documento == "cnpj":
#             if self.cnpj_eh_valido(documento):
#                 self.cnpj = documento
#             else:
#                 raise ValueError("CNPJ Inválido")
#         else:
#             raise ValueError("Documento Inválido")
#
#     def __str__(self):
#         if self.tipo_documento == "cpf":
#             return self.format_cpf()
#         elif self.tipo_documento == "cnpj":
#             return self.format_cnpj()
#
#     def cpf_eh_valido(self,cpf):
#         if len(cpf) == 11:
#             validador = CPF()
#             return validador.validate(cpf)
#         else:
#             raise ValueError("Quantidade de dígitos inválida")
#
#     def cnpj_eh_valido(self,cnpj):
#         if len(cnpj)==14:
#             validadaor_cnpj = CNPJ()
#             return validadaor_cnpj.validate(cnpj)
#         else:
#             raise ValueError("Quantidade de dígitos inválida")
#
#     def format_cpf(self):
#         mascara = CPF()
#         return mascara.mask(self.cpf)
#
#     def format_cnpj(self):
#         mascara= CNPJ()
#         return mascara.mask(self.cnpj)
