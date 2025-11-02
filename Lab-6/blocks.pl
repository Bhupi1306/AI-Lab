member_eq(X,[X|_]) :- !.
member_eq(X,[_|T]) :- member_eq(X,T).

goal_satisfied([], _).
goal_satisfied([G|Gs], State) :-
    member_eq(G, State),
    goal_satisfied(Gs, State).

block(a). block(b). block(c).

action_schema_instance(pickup(X)) :- block(X).
action_schema_instance(putdown(X)) :- block(X).
action_schema_instance(unstack(X,Y)) :- block(X), block(Y), X \= Y.
action_schema_instance(stack(X,Y)) :- block(X), block(Y), X \= Y.

action(pickup(X),
       [clear(X), ontable(X), holding(none)],
       [ontable(X), holding(none)],
       [holding(X)]).

action(putdown(X),
       [holding(X)],
       [holding(X)],
       [ontable(X), clear(X), holding(none)]).

action(unstack(X,Y),
       [on(X,Y), clear(X), holding(none), clear(Y)],
       [on(X,Y), clear(X), holding(none)],
       [holding(X), clear(Y)]).

action(stack(X,Y),
       [holding(X), clear(Y)],
       [holding(X), clear(Y)],
       [on(X,Y), clear(X), holding(none)]).

applicable(Action, State) :-
    action(Action, Preconditions, _, _),
    forall(member(P, Preconditions), member_eq(P, State)).

apply(Action, State, NewState) :-
    action(Action, Preconditions, Del, Add),
    forall(member(P, Preconditions), member_eq(P, State)),
    subtract(State, Del, S1),
    append(Add, S1, NewState).

redundant_move(pickup(X), [putdown(X)|_]).
redundant_move(putdown(X), [pickup(X)|_]).
redundant_move(stack(X,Y), [unstack(X,Y)|_]).
redundant_move(unstack(X,Y), [stack(X,Y)|_]).

plan_search(State, Goal, _, PathMoves, Plan) :-
    goal_satisfied(Goal, State),
    reverse(PathMoves, Plan).

plan_search(State, Goal, VisitedStates, PathMoves, Plan) :-
    length(PathMoves, Len), Len < 10,
    action_schema_instance(Action),
    applicable(Action, State),
    \+ redundant_move(Action, PathMoves),
    apply(Action, State, NewState),
    \+ member_eq(NewState, VisitedStates),
    plan_search(NewState, Goal, [State|VisitedStates], [Action|PathMoves], Plan).

plan(Init, Goal, Plan) :-
    plan_search(Init, Goal, [], [], Plan).

display_plan(Plan) :-
    (   Plan = [] ->
        writeln('No steps needed (Goal already satisfied).')
    ;   format('SUCCESS! Plan (~w steps):~n', [Plan]),
        display_steps(1, Plan)
    ).

display_steps(_, []).
display_steps(N, [Move|Rest]) :-
    format('~w. ~w~n', [N, Move]),
    N1 is N + 1,
    display_steps(N1, Rest).

test_simple :-
    Init = [ontable(a), ontable(b), ontable(c), clear(a), clear(b), clear(c), holding(none)],
    Goal = [on(a,b)],
    writeln('--- Test 1: Simple Stacking (Goal: on(a,b)) ---'),
    ( plan(Init, Goal, Plan) ->
        display_plan(Plan)
    ;
        writeln('FAILED - no plan found')
    ).

test_tower :-
    Init = [ontable(a), ontable(b), ontable(c), clear(a), clear(b), clear(c), holding(none)],
    Goal = [on(a,b), on(b,c)],
    writeln('--- Test 2: Tower Building (Goal: on(a,b), on(b,c)) ---'),
    ( plan(Init, Goal, Plan) ->
        display_plan(Plan)
    ;
        writeln('FAILED - no plan found')
    ).

test_complex :-
    Init = [ontable(a), on(b,a), ontable(c), clear(b), clear(c), holding(none)],
    Goal = [on(c,b)],
    writeln('--- Test 3: Complex Rearrangement (Goal: on(c,b)) ---'),
    ( plan(Init, Goal, Plan) ->
        display_plan(Plan)
    ;
        writeln('FAILED - no plan found')
    ).

run_all_tests :-
    test_simple, nl,
    test_tower, nl,
    test_complex, nl.
