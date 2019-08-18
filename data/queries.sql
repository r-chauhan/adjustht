/* USE CASE 1: Show the number of impressions and clicks that occurred 
before the 1st of June 2017, broken down by channel and country, 
sorted by clicks in descending order. */ 

select channel, country, sum(impressions) as impressions, sum(clicks) as clicks 
FROM `adjdata`
where date <= '2017-06-01' 
group by channel, country order by clicks desc;

/* USE CASE 2: Show the number of installs that occurred in May of 2017 on iOS, 
broken down by date, sorted by date in ascending order. */ 

select date, sum(installs) as installs
FROM `adjdata`
where date < '2017-06-01' AND date > '2017-05-01' AND os = 'ios' 
group by date order by date;

/* USE CASE 3: Show revenue, earned on June 1, 2017 in US, broken down by 
operating system and sorted by revenue in descending order. */ 

select os, sum(revenue) as revenue
FROM `adjdata`
where date = '2017-06-01' 
group by os order by revenue desc;

/* USE CASE 4: Show CPI and spend for Canada (CA) broken down by channel ordered by 
CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI. */ 

select channel, spend, avg(spend/installs) as cpi --cpi ?
FROM `adjdata`
where country = 'CA'
group by channel order by cpi desc