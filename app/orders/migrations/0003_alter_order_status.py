# Generated by Django 5.0 on 2024-02-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_payment_payment_method_id_payment_payment_type_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("New", "Criado"),
                    ("Accepted", "Aceito"),
                    ("await_payment", "Aguardando pagamento"),
                    ("payment_confirmed", "Pagamento Confirmado"),
                    ("waiting_for_shipping", "Aguardando Envio"),
                    ("sent", "Enviado"),
                    ("Completed", "Completo"),
                    ("Cancelled", "Cancelado"),
                ],
                default="New",
                max_length=21,
            ),
        ),
    ]