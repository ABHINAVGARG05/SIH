from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import DeliverySlot
from ml.predict import predict_best_time_slot


def success_page(request):
    return render(request, 'success.html')


def schedule_delivery(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        receiver = request.POST.get('receiver')
        available_times = request.POST.get('available_times')  # JSON input
        
        # Convert available times to the required format
        # user_pref = UserPreference.objects.get_or_create(user=receiver)[0]
        # user_pref.available_times = available_times
        # user_pref.save()
        
        # Predict the best time slot using AI model
        #best_slot = predict_best_time_slot(user_pref.available_times)

        # Create a new delivery slot entry
        delivery = DeliverySlot.objects.create(
            sender=sender,
            receiver=receiver,
            preferred_time=best_slot
        )
        return JsonResponse({"message": "Delivery scheduled successfully", "preferred_time": best_slot})
def create_delivery(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        receiver_name = request.POST.get('receiver_name')
        delivery_address = request.POST.get('delivery_address')
        delivery_time_slot = request.POST.get('delivery_time_slot')

        # Create a new delivery slot entry based on form inputs
        try:
            delivery = DeliverySlot.objects.create(
                sender_name=sender_name,
                receiver_name=receiver_name,
                delivery_address=delivery_address,
                delivery_time_slot=delivery_time_slot,
            )
            return redirect('success_page')  # Redirect to the create delivery page or another page
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return render(request, 'delivery/create.html')
    # Render the create.html page for GET requests
