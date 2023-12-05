{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "614f29d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "tuple1=(3,4,5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b13e478",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "663efb95",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 4, 5, 6)\n"
     ]
    }
   ],
   "source": [
    "print(tuple1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2c8b6e73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "()\n",
      "(5, 7, 8, 3)\n",
      "('mouse', [1, 2, 3, 4], [4, 5, 6, 7])\n"
     ]
    }
   ],
   "source": [
    "#different types of tuples\n",
    "my_tuple=()\n",
    "print(my_tuple)\n",
    "#ntegers\n",
    "my_tuple=(5,7,8,3)\n",
    "print(my_tuple)\n",
    "#tuple with mixed datatypes\n",
    "my_tuple=(5,\"hello\",3.7)\n",
    "#tuple with nested dtatypes\n",
    "my_tuple=(\"mouse\",[1,2,3,4],[4,5,6,7])\n",
    "print(my_tuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "312041d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "([1, 2, 3, 4],)\n"
     ]
    }
   ],
   "source": [
    "print(my_tuple[1:2])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d52226e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('mouse', [1, 2, 3, 4], [4, 5, 6, 7])\n"
     ]
    }
   ],
   "source": [
    "print(my_tuple[:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "66850742",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 6, 4, 7, 2)\n"
     ]
    }
   ],
   "source": [
    "tuple1=(3,6,4,7,2)\n",
    "print(tuple1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9b541640",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(tuple1[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f5604a95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple1.index(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f19c622e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple1.count(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "08fea923",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 3, 4, 6, 7]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(tuple1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "976d1439",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[7, 6, 4, 3, 2]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(tuple1,reverse=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e2155a54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 4, 5, 6, 3, 5, 6, 5, 4, 4)\n"
     ]
    }
   ],
   "source": [
    "tuple2=(3,4,5,6,3,5,6,5,4,4,)\n",
    "print(tuple2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "bf8b837f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "l=len(tuple2)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0eaa9efc",
   "metadata": {},
   "source": [
    "TUPLE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "99916bce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "45"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(tuple2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7039bdfc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(tuple2,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "476071c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3.4, 'deepu', 5, 2, 'Rani', 2)\n"
     ]
    }
   ],
   "source": [
    "tuple3=(2,3.4,\"deepu\",5,2,\"Rani\",2)\n",
    "print(tuple3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "4fbdfd99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple3.count(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "96998070",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3.4, 'deepu')\n"
     ]
    }
   ],
   "source": [
    "print(tuple3[1:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "014a3f4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3.4, 'deepu')\n"
     ]
    }
   ],
   "source": [
    "print(tuple3[0:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1f4f694c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "languages=(\"python\",\"java\",\"c\")\n",
    "print(\"c\" in languages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3c559ef0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(\"c++\"in languages)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "35deafa0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python\n",
      "java\n",
      "c\n"
     ]
    }
   ],
   "source": [
    "for language in languages:\n",
    "    print(language)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48ea0142",
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
