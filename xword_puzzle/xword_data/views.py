from django.shortcuts import render

# Create your views here.

def create_note(request):
    print('create_note')
    data = request.data

    note = Note.objects.create(
        body=data['body']
    )

    serializer = NoteSerializer(instance=note, many=False)
    return Response(serializer.data)
