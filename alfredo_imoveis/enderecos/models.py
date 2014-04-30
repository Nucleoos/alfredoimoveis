# encoding:utf-8
from django.db import models
from django.db.models import signals

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length = 150, null = False, blank = False, verbose_name = 'Cidade')
    uf = models.CharField(max_length = 2,   null = False, blank = False)
    pais = models.CharField(max_length = 50,  null = False, blank = False)

    def __unicode__(self):
        return self.nome + " - " + self.uf

    class Meta:
        verbose_name = u'Município'
        verbose_name_plural = u'Municípios'

class Bairro(models.Model):
    nome = models.CharField(max_length = 150, null = False, blank = False,
                            verbose_name = 'Bairro', help_text='Informe o nome do bairro')
    cidade = models.ForeignKey(Cidade)
    codigo = models.IntegerField('Código',null = True, blank = True)

    def __unicode__(self):
        return self.nome + " - " + self.cidade.nome

def insere_codigo(**kwargs):
    bairro = kwargs['instance']
    bairro.codigo = bairro.id
    models.signals.post_save.disconnect(insere_codigo, sender=Bairro,
                            dispatch_uid="enderecos.models.Bairro")
    bairro.save()
    models.signals.post_save.connect(insere_codigo, sender=Bairro,
                            dispatch_uid="enderecos.models.Bairro")

models.signals.post_save.connect(insere_codigo, sender=Bairro,
                            dispatch_uid="enderecos.models.Bairro")

class Endereco(models.Model):
    rua = models.CharField(max_length = 150, null  = False, blank = False)
    numero = models.IntegerField(null = False,  blank = False               )
    bairro = models.ForeignKey(Bairro, null = False,  blank = False)
    cep = models.CharField(max_length = 9,   null  = True, blank = True)

    def __unicode__(self):
        return self.rua + " - " + unicode(self.numero) + " - " + self.bairro.nome + " - " + self.cep + " - " + self.bairro.cidade.nome
