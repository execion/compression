from os import listdir, getcwd
from os.path import join, getmtime, exists, isdir
from shutil import make_archive
from datetime import datetime
from argparse import ArgumentParser
from helper.logger import Logger

args = ArgumentParser()

args.add_argument("--origin", type=str, required=True)

args_value = args.parse_args()

home = getcwd()
log_folder = join(home, 'log')
output = join(home, 'output')
origin = args_value.origin

log_file = "compress_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"

logger = Logger(join(log_folder, log_file))

logger.info("Inicia el proceso")
for carpeta in listdir(origin):
    if not isdir(join(origin, carpeta)):
        logger.info(f"No es un directorio: {carpeta}")
        continue
    if exists(join(output, f'{carpeta}.zip')): # Si para ese folder a comprimir ya existe una compresion anterior
        if datetime.fromtimestamp(getmtime(join(origin,carpeta))) > datetime.fromtimestamp(getmtime(join(output, f'{carpeta}.zip'))): # Compara las ultimas modificaciones entre la compresion anterior y el folder a comprimir
            logger.info(f"Se crea el archivo: {join(origin, carpeta)}")
            make_archive(join(output, carpeta),'zip',join(origin, carpeta))
        else:
            logger.info(f"La carpeta {carpeta} ya esta comprimida")
    else:
        logger.info(f"Se crea el archivo: {join(origin, carpeta)}")
        make_archive(join(output, carpeta),'zip', join(origin, carpeta))

logger.info("Finaliza el proceso")
exit(0)