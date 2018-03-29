from django.core.management.base import BaseCommand, CommandError
from main.models import Cities, CountryCode


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        file_path = "/home/user-15/Загрузки/worldcitiespop.txt"
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            for line in file:
                new_row_list = line.split(",")
                city = Cities(city=new_row_list[1],
                              accent_city=new_row_list[2],
                              region=new_row_list[3],
                              population=new_row_list[4],
                              latitude=new_row_list[5],
                              longitude=new_row_list[6])
                country_code = CountryCode.objects.get_or_create(title=new_row_list[0])
                city.country_code = country_code
                city.save()
                self.stdout.write("Unterminated line")
