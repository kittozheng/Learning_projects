@extends('admin._layouts.default')

@section('main')

	{{ Notification::showAll() }}
	
	<a href="{{ URL::route('admin.articles.create') }}" class="btn btn-primary">Create</a>

	<table class="table table-striped">
		<thead>
			<tr>
				<th>#</th>
				<th>Title</th>
				<th>Last updated</th>
				<th><i class="icon-cog"></i></th>
			</tr>
		</thead>
		<tbody>
			@foreach($articles as $article)
				<tr>
					<td>{{ $article->id }}</td>
					<td><a href="{{ URL::route('admin.articles.show', $article->id )}}">{{ $article->title }}</td>
					<td>{{ $article->updated_at }}</td>
					<td>
						<a href="{{ URL::route('admin.articles.edit', $article->id) }}" class="btn btn-success btn-mini pull-left">Edit</a>
						{{ Form::open(array('route' => array('admin.articles.destroy', $article->id), 'method' => 'delete', 'data-confirm' => 'Are you sure?')) }}
							<button type="submit" href="{{ URL::route('admin.articles.destroy', $article->id) }}" class="btn btn-danger btn-mini">Delete</button>
						{{ Form::close() }}		
					</td>
				</tr>
			@endforeach
		</tbody>
	</table>

@stop