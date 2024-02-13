from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class ItemDashboardView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stock_status = request.query_params.get('stock_status')

        # Filter inventory items based on stock_status query parameter
        items = InventoryItem.objects.filter(owner=request.user)
        if stock_status:
            items = items.filter(stock_status=stock_status)

        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
