from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This Command creates houserules"
    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="Now many times do you want me to tell you that I love you"
    #     )

    def handle(self, *args, **options):
        house_rules = [
            "Don't smoke",
            "Kepp Quiet",
        ]

        for r in house_rules:
            HouseRule.objects.create(name=r)
        self.stdout.write(
            self.style.SUCCESS(f"{len(house_rules)} house_rules Created!")
        )
