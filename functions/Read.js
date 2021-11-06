// JavaScript source code
import { createClient } from '@supabase/supabase-js'

url = 'https://uxdydupspijujofdyxug.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaWF0IjoxNjM2MTc0MzIzLCJleHAiOjE5NTE3NTAzMjN9.M3_cTtMyV5eDLo8QLlyOgpD2YS4uGDz9DLIKQca7Rvs'
const supabase = createClient(url, key)

let { data: notes, error } = await supabase
	.from('D2NYUAD-DB')
	.select('time, num')