def delete_oldest_items(limit, model):
    count = model.objects.exclude(dont_delete=True).count() 
    if count > limit:
        items_to_delete = count - limit
        # Query for the oldest items, excluding those with dont_delete=True
        oldest_items = model.objects.exclude(dont_delete=True).order_by('created_at')[:items_to_delete]
        for item in oldest_items:
            if not item.dont_delete:
                item.delete()
            else:
                pass

        # print(f'Deleted {items_to_delete} oldest items from {model}')