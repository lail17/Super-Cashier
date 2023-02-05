#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import modul Super_Cashier

import Super_Cashier as sc


# ### TEST 1

# In[ ]:


#test 1 (add_item())

trnsct_123 = sc.Transaction()
trnsct_123.add_item("Ayam Goreng", 2, 20_000)
trnsct_123.add_item("Pasta Gigi", 3, 15_000)


# In[ ]:


#cek data yang sudah masuk

trnsct_123.print_item()


# ### TEST 2

# In[ ]:


#test 2 (delete_item())

trnsct_123.delete_item("Pasta Gigi")


# ### TEST 3

# In[ ]:


#test 3 (reset_transaction)

trnsct_123.reset_transaction()


# ### TEST 4

# In[ ]:


#test 4 (total_price())

#tambahkan kembali data yang sudah di reset
trnsct_123.add_item("Ayam Goreng", 2, 20_000)
trnsct_123.add_item("Pasta Gigi", 3, 15_000)
trnsct_123.add_item("Mainan Mobil", 1, 200_000)
trnsct_123.add_item("Mi Instan", 5, 3_000)


# In[ ]:


trnsct_123.total_price()


# In[ ]:




