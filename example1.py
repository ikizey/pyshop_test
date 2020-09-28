# продолжите функцию live_search() на Python таким образом, чтобы она возвращала
# список товаров (список объектов Product упакованные в JSON в произвольном формате)
# которые содержат строку q в полях sku, name или description в любом регистре символов.
def live_search(request, template_name="shop/livesearch_results.html"):
    q = request.GET.get("q", "")
    qs = Product.objects.filter(
        Q(sku__icontains=q)
        | Q(name__icontains=q)
        | Q(description__icontains=q)
    )
    context = {"data": serializers.serialize("json", qs)}
    return render(request, template_name, context)
