{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "329ef548",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{101: 'python', 102: 'SQL', 103: 'Tableau'}\n"
     ]
    }
   ],
   "source": [
    "dic1={101:'python',\n",
    "     102:'SQL',\n",
    "     103:'Tableau'}\n",
    "print(dic1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "df91d77a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys([101, 102, 103])\n"
     ]
    }
   ],
   "source": [
    "print(dic1.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b75fc01b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SQL\n"
     ]
    }
   ],
   "source": [
    "a=dic1.get(102)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3183b113",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{101: 'python', 102: 'SQL', 103: 'Tableau', 104: 'powerBI'}\n"
     ]
    }
   ],
   "source": [
    "d2={104:'powerBI'}\n",
    "dic1.update(d2)\n",
    "print(dic1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "da3ec166",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "d2.clear()\n",
    "print(d2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a37febdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{101: 'python', 102: 'SQL', 103: 'Tableau', 104: 'powerBI'}\n"
     ]
    }
   ],
   "source": [
    "print(dic1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a8b0424e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'deepu': 123, 'sri': 456}\n"
     ]
    }
   ],
   "source": [
    "d3={\"deepu\":123,\"sri\":456}\n",
    "print(d3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "df4f33ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "empty_dic={}\n",
    "print(empty_dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9dd8e844",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SQL\n"
     ]
    }
   ],
   "source": [
    "#retrieving the data\n",
    "print(dic1.pop(102))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "51ae68f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{101: 'python', 103: 'Tableau', 104: 'powerBI'}\n"
     ]
    }
   ],
   "source": [
    "print(dic1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b36f5be6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{105: 'java'}\n"
     ]
    }
   ],
   "source": [
    "#the popitrem() method this will remove(key,value) from the dictinary Last in first out(LIFO) method\n",
    "dic1={105:\"java\"}\n",
    "print(dic1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5fd3be06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(105, 'java')\n"
     ]
    }
   ],
   "source": [
    "print(dic1.popitem())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8d4d462a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "print(dic1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c82e90d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
