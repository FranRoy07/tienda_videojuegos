from django.contrib import admin
from .models import Carrito, ItemCarrito
# Register your models here.

# Inline para mostrar los ítems dentro del carrito
class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0  # No mostrar filas vacías adicionales
    readonly_fields = ('subtotal',)  # Subtotal solo lectura

# Admin del carrito
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total_items', 'total_precio', 'creado', 'actualizado')
    search_fields = ('usuario__username',)  # Buscar carritos por nombre de usuario
    inlines = [ItemCarritoInline]

# Admin de los ítems (opcional, también accesible por separado)
@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'juego', 'cantidad', 'subtotal')
    list_filter = ('carrito',)
    search_fields = ('juego__nombre',)
    readonly_fields = ('subtotal',)
    
    