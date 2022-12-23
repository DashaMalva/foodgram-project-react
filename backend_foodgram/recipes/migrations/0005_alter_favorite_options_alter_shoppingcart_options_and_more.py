# Generated by Django 4.1.4 on 2022-12-22 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0004_alter_shoppingcart_recipe_in_cart_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['recipe', 'user'], 'verbose_name': 'Избранный рецепт', 'verbose_name_plural': 'Избранные рецепты'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ['recipe', 'user'], 'verbose_name': 'Рецепт из списка покупок', 'verbose_name_plural': 'Список покупок'},
        ),
        migrations.RemoveConstraint(
            model_name='favorite',
            name='unique_user_favorite_recipe',
        ),
        migrations.RemoveConstraint(
            model_name='shoppingcart',
            name='unique_user_recipe_in_cart',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='favorite_recipe',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='recipe_in_cart',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_user_favorite_recipe'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_user_recipe_in_cart'),
        ),
    ]