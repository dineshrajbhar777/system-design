# Full Requirement Specification

## 1. Parking Capacity

* The parking building has a total of:
  * 50 Small parking spaces
  * 100 Medium parking spaces
  * 30 Large parking spaces

## 2. Vehicle Entry

* A customer drives onto a lift with a terminal next to it.
* The system automatically measures and classifies the car as either Small, Medium, or Large using sensors.
* The terminal displays the number of available spots for that vehicle type.

## 3.Parking Process

* If there are open spaces, the customer can confirm to proceed.
* The system automatically assigns a parking spot for the vehicle.
* The lift transports the vehicle to the appropriate floor or area and parks it autonomously.
* The system stores vehicle and spot information (e.g., size, ID, assigned spot).

## 4.Vehicle Exit

* The customer can initiate checkout at the terminal.
* The system locates the parked vehicle using its ID.
* The lift retrieves and delivers the vehicle to the exit.
* The parking spot is freed and marked as available.

## 5. System Features

* Real-time tracking of all parking spot occupancy
* Efficient allocation of spots by vehicle size
* Optionally support future extensions like:
    * Reservation system
    * Billing per hour
    * Admin dashboard