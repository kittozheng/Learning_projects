<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the Closure to execute when that URI is requested.
|
*/
// get request
Route::get('/', function()
{
	return View::make('hello');
});

// post request
Route::post('foo', function(){
	return 'Hello World';
});

// // get/post request
// Route::match(array('GET', 'POST'), '/', function(){
// 	return 'Hello World';
// });

// // any request
// Route::any('foo', function(){
// 	return 'Hello World';
// });

// // https request
// Route::get('foo', array('https', function(){
// 	return 'Must be over HTTPS';
// }));

// // paramter withoud default value
// Route::get('user/{name?}', function($name=null){
// 	return $name;
// });

// // parameter with default value
// Route::get('user/{name?}', function($name='Jhon'){
// 	return $name;
// });

// // parameter with re _pattern
// Route::get('user/{name}', function($name){
// 	//
// })
// ->where('name', '[A-Za-z]+');
// Route::get('user/{id}', function($id){
// 	//
// })
// ->where('name', '[0-9]+');

// parameters_array with re_pattern
// Route::get('user/{id}/{name}', function($id, $name){
// 	//
// })
// ->where(array('id' => '[0-9]+', 'name' => '[a-z]+'));

//  setting global re
// Route::pattern('id', '[0-9]+');

//set paramter outside url setting
// Route::filter('foo', function(){
// 	if(Route::input('id') == 1){
// 		//
// 	}
// });

// filter configuration
// Route::filter('old', function()){
// 	if(Input::get('age') < 200){
// 		return Redirect::to('/');
// 	}
// }

// add filter to route
// Route::get('user', array('before' => 'old', function(){
// 	return 'You are over 200 years old';
// }))

// Route::get('user', array('before' => 'old', 'uses' => 'UserController@showProfile'));

// add multiple filters to multiple route
// Route::get('user', array('before' => 'auth | old', function(){
// 	return 'You are authenticated and over 200 years old'
// }));


// Route::get('admin/logout', array('as' => 'admin.logout', 'uses' => 'App\Controllers\Admin\AuthController@getLogout'));
// Route::get('admin/login', array('as' => 'admin.login', 'uses' => 'App\Controllers\Admin\AuthController@getLogin'));
// Route::post('admin/login', array('as' => 'admin.login.post', 'uses' => 'App\Controllers\Admin\AuthController@postLogin'));

// Route::group(array('prefix' => 'admin', 'before' => 'auth.admin'), function(){
// 	Route::any('/', 'App\Controllers\Admin\PagesController@index');
// 	Route::resource('article', 'App\Controllers\Admin\ArticlesController');
// 	Route::resource('pages', 'App\Controllers\Admin\PagesController');
// });

Route::get('admin/logout', array('as' => 'admin.logout', 'uses' => 'App\Controllers\Admin\AuthController@getLogout'));
Route::get('admin/login', array('as' => 'admin.login', 'uses' => 'App\Controllers\Admin\AuthController@getLogin'));
Route::post('admin/login', array('as' => 'admin.login.post', 'uses' => 'App\Controllers\Admin\AuthController@postLogin'));

Route::group(array('prefix' => 'admin', 'before' => 'auth.admin'), function()
{
    Route::any('/', 'App\Controllers\Admin\PagesController@index');
    Route::resource('articles', 'App\Controllers\Admin\ArticlesController');
    Route::resource('pages', 'App\Controllers\Admin\PagesController');
});