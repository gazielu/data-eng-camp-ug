select count(distinct index) from green_taxi_trips
where to_char(lpep_pickup_datetime,'DD-MM-YYYY') = '15-01-2019'
and   to_char(lpep_dropoff_datetime,'DD-MM-YYYY') = '15-01-2019'
--20530
-- --by largest trip by 
-- select to_char(lpep_pickup_datetime,'DD-MM-YYYY') as dateid, max(trip_distance) from green_taxi_trips
-- group by to_char(lpep_pickup_datetime,'DD-MM-YYYY')
-- order by max(trip_distance) desc
-- 15-01-2019  - 117.99
-- 15-01-2019

--by largest trip by day
select to_char(lpep_pickup_datetime,'DD-MM-YYYY') as dateid, sum(trip_distance) from green_taxi_trips
group by to_char(lpep_pickup_datetime,'DD-MM-YYYY')
order by max(trip_distance) desc
--75856
select passenger_count, count(passenger_count) as count_passanger from green_taxi_trips 
where  to_char(lpep_pickup_datetime,'DD-MM-YYYY') = '01-01-2019'
and passenger_count in ( 2,3)
group by passenger_count
--1282 254

select p."DOLocationID",sum(tip_amount),dropoff."Zone" as Dropoff from green_taxi_trips p 
left join pickup_zone dropoff
on dropoff."LocationID" = p."DOLocationID"
inner join pickup_zone pu
on pu."LocationID" = p."PULocationID"
where pu."Zone" = 'Astoria'
group by p."DOLocationID",dropoff."Zone",p."DOLocationID"
order by max(tip_amount) desc
limit 1
--long island  800.32

--
