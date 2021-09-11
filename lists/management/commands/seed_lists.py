import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models
from django.contrib.admin.utils import flatten

NAME = "lists"


class Command(BaseCommand):

    help = f"This Command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help=f"Now many {NAME} you create?"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[
                random.randint(0, 5) : random.randint(6, 30)
            ]  # query set list of room
            list_model.rooms.add(*to_add)  # 쿼리 내의 요소를 가져오기 위함
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} Created!"))
