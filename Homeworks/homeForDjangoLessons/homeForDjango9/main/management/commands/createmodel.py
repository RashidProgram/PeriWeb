from django.core.management.base import BaseCommand, CommandError
from main.models import Cities


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        file_path = "/home/rashid/Downloads/worldcitiespop.txt"
        with open(file_path, 'r') as file:
            for line in file:
                new_row_list = line.split(",")
                print(new_row_list[0],
                      new_row_list[1],
                      new_row_list[2],
                      new_row_list[3],
                      new_row_list[4],
                      new_row_list[5],
                      new_row_list[6], end="\n-----------------------------------------\n")
                """city = Cities(city=new_row_list[1],
                               accent_city=new_row_list[2],
                               region=new_row_list[3],
                               population=new_row_list[4],
                               latitude=new_row_list[5],
                               longitude=new_row_list[6])
                country_code = CountryCode.objects.get_or_create(title=new_row_list[0])
                city.country_code = country_code
                city.save()"""
                self.stdout.write("Unterminated line")
