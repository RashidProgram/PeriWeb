from django.core.management.base import BaseCommand, CommandError
from main.models import Cities, CountryCode


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            file_path = '/home/'.format(options["path"])
        except KeyError:
            try:
                file_path = '/home/'.format(args[0])
            except IndexError:
                file_path = "/home/rashid/Downloads/worldcitiespop.txt"
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            i = 1
            for line in file:
                if i == 1:
                    continue
                new_row_list = line.split(",")
                new_row_list[4] = new_row_list[4] if new_row_list[4] != "" else 0
                print(new_row_list[4])
                city = Cities(city=new_row_list[1],
                              accent_city=new_row_list[2],
                              region=new_row_list[3],
                              population=new_row_list[4],
                              latitude=new_row_list[5],
                              longitude=new_row_list[6])
                country, created = CountryCode.objects.get_or_create(title=new_row_list[0])
                city.country = country
                city.save()
            self.stdout = "Unterminated line"
