<?php

namespace App\Controllers\Admin;

use Article;
use Input, Notification, Redirect, Sentry, Strl;

use App\Services\Validators\ArticleValidator;

class ArticlesController extends \BaseController {

	/**
	 * Display a listing of the resource.
	 * GET /admin/articles
	 *
	 * @return Response
	 */
	public function index()
	{
		return \View::make('admin.articles.index')->with('articles',  Article::all());
	}

	/**
	 * Show the form for creating a new resource.
	 * GET /admin/articles/create
	 *
	 * @return Response
	 */
	public function create()
	{
		return \View::make('admin.articles.create');
	}

	/**
	 * Store a newly created resource in storage.
	 * POST /admin/articles
	 *
	 * @return Response
	 */
	public function store()
	{
		$validation = new ArticleValidator;

		if($validation->passes()){
			$article 			= 	new Article;
			$article->title 		=	Input::get('title');
			$article->body 		= 	Input::get('body');
			$article->image 		= 	Input::get('image') ;
			$article->user_id	=	Sentry::getUser()->id;

			$article->save();
		
			Notification::success("New Article Add!");

			return Redirect::route('admin.articles.edit', $article->id);
		}
	}

	/**
	 * Display the specified resource.
	 * GET /admin/articles/{id}
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function show($id)
	{
		return \View::make('admin.articles.show')->with('article', Article::find($id));
	}

	/**
	 * Show the form for editing the specified resource.
	 * GET /admin/articles/{id}/edit
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function edit($id)
	{
		return \View::make('admin.articles.edit')->with('articles', Article::find($id));
	}

	/**
	 * Update the specified resource in storage.
	 * PUT /admin/articles/{id}
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function update($id)
	{
		$validation = new ArticleValidator;

		if($validation->passes()){
			$article 			= 	Article::find($id);
			$article->title 		=	Input::get('title');
			$article->body 		= 	Input::get('body');
			$article->image 		= 	Input::get('image') ;
			$article->user_id	=	Sentry::getUser()->id;

			$article->save();
		
			Notification::success("Article Update!");

			return Redirect::route('admin.articles.edit', $article->id);
		}

		return Redirect::back()->withInput()->withErrors($validation->errors);
	}

	/**
	 * Remove the specified resource from storage.
	 * DELETE /admin/articles/{id}
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function destroy($id)
	{
		$article = Article::find($id);
		$article->delete();

		Notification::success('article deleted!');

		return Redirect::route('admin.article.index');
	}

}