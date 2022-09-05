# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ls_test.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spuustin <spuustin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/05 16:46:13 by spuustin          #+#    #+#              #
#    Updated: 2022/09/05 18:01:46 by spuustin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os, stat

# HOW TO:
# run on command line: 
# python3 ls_test.py <path of ls_project>

# creating setuid/setgid/stickybit -testfiles

def create_files(path):
	files = {"/uidi": 0o2775, "/uidiS": 0o2666, "/gidi": 0o4775, "/gidiS": 0o4666, 
			"/sticky": 0o1775, "/stickyT": 0o1666}

	for name in files:
		f = open(path + name, "x")
		os.chmod(path + name, files[name])
		f.close()

if len(sys.argv) != 2:
	print("exactly one argument needed!\ntry 'python3 ls_test.py <path_of_dir>'")
else:
	path = sys.argv[1];
	create_files(path)
