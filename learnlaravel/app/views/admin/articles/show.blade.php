@extends('admin._layouts.default')

@section('main')

	<h2>Article Content</h2>

	<div id="onepage">

	<div class="title">
		<h3>{{ $article->title }}</h3>
	</div>

	<div class="image_url">
		<h3>{{ $article->image }}</h3>
	</div>

	<div class="info">
		{{ $author }} pulished at {{ $article->created_at }}  and last updated {{ $article->updated_at }}
	</div>

	<div class="body">
		{{ $article->body }}
	</div>

	</div>

@stop